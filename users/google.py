import google.oauth2.credentials
import google_auth_oauthlib.flow
from google.oauth2 import id_token
from google.auth.transport import requests

flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    {"./my_settings.py"},
    scopes = [
        'openid',
        'https://www.googleapis.com/auth/userinfo.email',
        'https://www.googleapis.com/auth/userinfo.profile'
    ],
    state = '12345678910',
)

flow.redirect_uri = 'http://localhost:8000/'

authorization_url, state = flow.authorization_url(
    access_type='offline',
    include_granted_scopes='true')
    
    
def verify_id_token(credentials):
    idinfo = id_token.verify_oauth2_token(credentials.id_token, 
        requests.Request(),
        secret_keys.google_client_id
    )
    return idinfo

def verify_id_token_form_uri(uri):
    flow.fetch_token(authorization_response=uri)
    return verify_id_token(flow.credentials)