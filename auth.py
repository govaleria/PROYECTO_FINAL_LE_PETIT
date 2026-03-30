from authlib.integrations.flask_client import OAuth

oauth = OAuth()

auth0 = oauth.register(
    'auth0',
    client_id='YgPJMTUuVnFdgnE5GGwMphb1MrCFAQcs',
    client_secret='H1w2rtJ2Y5y7U-4HPvhiKy-t_1AOZxvRsumQCCYolrBqPtk065xV5NrZQz8O8RVT', # <--- ¡Pégalo aquí directamente!
    server_metadata_url='https://dev-a7pcxol1levay1br.us.auth0.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid profile email',
        'token_endpoint_auth_method': 'client_secret_post', # Esto es vital para evitar el Unauthorized
    }
)