from backend.config import settings
import urllib.parse


def generate_google_oautn_redirect_uri():
    query_params = {
        'redirect_uri': 'http://127.0.0.1:5500/auth/google',
        'client_id': settings.OAUTH_GOOGLE_CLIENT_ID,
        'response_type': 'code',
        'scope': " ".join([
            'https://www.googleapis.com/auth/drive',
            'https://www.googleapis.com/auth/calendar',
            'openid',
            'profile',
            'email',
        ]),
        'access_type':'offline',
        #statr ...
    }
    

    
    
    query_string = urllib.parse.urlencode(query_params, quote_via=urllib.parse.quote)
    base_url = 'https://accounts.google.com/o/oauth2/v2/auth'
    return f"{base_url}?{query_string}"