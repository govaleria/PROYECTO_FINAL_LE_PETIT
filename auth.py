from authlib.integrations.flask_client import OAuth

oauth = OAuth()

auth0 = oauth.register(
    'auth0',
    client_id='c4tldiH9hMwEo1ZXrJFJb2PhmPkkTnKy',
    client_secret='5D8j06adOIiqwVNq_4pD5tHhHDh90jQ2wQ0MeOc1Ni48Dd7lE7GMu4csv4bqP1YV', # <--- ¡Pégalo aquí directamente!
    server_metadata_url='https://dev-a1rj4fpr7sm4p47r.us.auth0.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid profile email',
        'token_endpoint_auth_method': 'client_secret_post', # Esto es vital para evitar el Unauthorized
    }
)