import os
from flask import Flask, redirect, render_template, request, url_for, session
from auth import auth0, oauth
from models import Cliente, SessionLocal
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
# Esta llave es vital para que la sesión no falle
app.secret_key = "una_clave_muy_secreta_123"
oauth.init_app(app)

@app.route('/')
def index():
    user = session.get('user')
    return render_template('index.html', user=user)

@app.route('/login')
def login():
    # Forzamos la redirección a 127.0.0.1 para que Auth0 no te rechace
    return auth0.authorize_redirect(redirect_uri="http://127.0.0.1:5000/callback")

@app.route('/callback')
def callback(): # Quitamos 'async' para simplificar
    try:
        # Obtenemos el token sin 'await'
        token = auth0.authorize_access_token()
        user = token.get('userinfo')
        
        if user:
            session['user'] = user
            
            # Registro en MySQL (Punto 3.1)
            db = SessionLocal()
            cliente_db = db.query(Cliente).filter(Cliente.correo == user['email']).first()

            if not cliente_db:
                nuevo_cliente = Cliente(
                    nombre=user['name'], 
                    correo=user['email'],
                    password="auth0_user" # Contraseña dummy para usuarios de Auth0
                )
                db.add(nuevo_cliente)
                db.commit()
            db.close()

            return redirect(url_for('completar_perfil'))
        
    except Exception as e:
        # Si sale error aquí, limpia la sesión e intenta de nuevo
        session.clear()
        return f"Error en callback: {str(e)}. Por favor, intenta en modo incógnito.", 400

@app.route('/completar-perfil', methods=['GET', 'POST'])
def completar_perfil():
    user = session.get('user')
    if not user:
        return redirect(url_for('login'))

    if request.method == 'POST':
        tipo_doc = request.form.get('tipo_doc')
        num_doc = request.form.get('num_doc')

        db = SessionLocal()
        cliente = db.query(Cliente).filter(Cliente.correo == user['email']).first()
        if cliente:
            cliente.tipo_documento = tipo_doc
            cliente.numero_documento = num_doc
            db.commit()
        db.close()

        return redirect(url_for('profile'))

    return render_template('completar_perfil.html', user=user)

@app.route('/profile')
def profile():
    user = session.get('user')
    if not user:
        return redirect(url_for('login'))
    
    db = SessionLocal()
    cliente = db.query(Cliente).filter(Cliente.correo == user['email']).first()
    db.close()
    
    return render_template('profile.html', user=user, cliente_db=cliente)

@app.route('/logout')
def logout():
    session.clear()
    # Cambia los datos por los tuyos si no usas .env
    return redirect(
        "https://dev-a1rj4fpr7sm4p47r.us.auth0.com/v2/logout?"
        "client_id=c4tldiH9hMwEo1ZXrJFJb2PhmPkkTnKy&"
        "returnTo=http://127.0.0.1:5000/"
    )
    
    return redirect(
        f"https://{domain}/v2/logout?"
        f"client_id={client_id}&"
        f"returnTo={url_for('index', _external=True)}"
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)