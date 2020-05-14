import os
import jwt
import hashlib
import requests
import json
from datetime import datetime, timedelta
from ..services import util, sqlite

def oauth_urls():
    ret = {}
    ret['github'] = f"https://github.com/login/oauth/authorize?client_id={os.environ.get('GITHUB_CLIENT_ID')}"
    return ret

def get_details(id):
    query = "SELECT * FROM users WHERE id = ?"
    params = (id,)
    return sqlite.read(query, params, one=True)

def lookup(oauth):
    query = "SELECT * FROM users WHERE oauth = ?"
    params = (oauth,)
    return sqlite.read(query, params, one=True)

def create_login_token(sub):
    return jwt.encode({
        'sub': sub,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=60*24*30)
    }, get_secret_token())

def get_user_data_from_token(token):
    token_dict = verify_token(token)
    if not token_dict:
        util.logger.error(f'Could not verify token: {token}')
        return False
    return lookup(token_dict.get('sub'))

def get_secret_token():
    return os.environ.get('JWT_SIGNING_TOKEN')

def verify_token(token):  
    try: 
        response = jwt.decode(token, get_secret_token())
    except:
        util.logger.error(f'Bad token: {token}')
        return False
    return response

def find_or_create_user(oauth, profile):
    user_hash = hashlib.sha224(oauth.encode('ascii')).hexdigest()
    query = "INSERT INTO users (oauth, profile, last_login) VALUES (?, ?, strftime('%Y-%m-%dT%H:%M:%fZ', 'now')) ON CONFLICT (oauth) DO UPDATE SET profile = ?, last_login = strftime('%Y-%m-%dT%H:%M:%fZ', 'now')"
    params = (user_hash, json.dumps(profile), json.dumps(profile))
    if not sqlite.write(query, params):
        return False
    return user_hash

def github_login(token):
    auth_response = github_token_to_access_code(token)
    if not auth_response:
        return False
    user_profile = github_get_user_profile(auth_response.get('access_token'))
    if not user_profile:
        return False
    return user_profile

def github_token_to_access_code(token):
    payload = {
        'client_id': os.environ.get('GITHUB_CLIENT_ID'),
        'client_secret': os.environ.get('GITHUB_CLIENT_SECRET'),
        'code': token
    }
    response = requests.post("https://github.com/login/oauth/access_token", data=payload, headers={'Accept': 'application/json'})
    if response.status_code != 200:
        return False
    return response.json()

def github_get_user_profile(oauth_token):
    response = requests.get("https://api.github.com/user", headers={'Authorization': f"token {oauth_token}"})
    if response.status_code != 200:
        return False
    return response.json()
