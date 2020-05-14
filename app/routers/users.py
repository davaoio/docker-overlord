from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel
from typing import List
from ..services import util, users

router = APIRouter()

class LoginToken(BaseModel):
    value: str

@router.get("/oauth-urls")
def oauth_urls():
    return users.oauth_urls()

@router.post("/github")
def login_github(token: LoginToken):
    profile = users.github_login(token.value)
    if not profile:
        raise HTTPException(status_code=403, detail="Invalid Authentication Token")
    user_hash = users.find_or_create_user(f"github||{profile.get('id')}", profile)
    util.logger.warning(f"GitHub Account Logged In: {user_hash} ({profile.get('id')})")
    if not user_hash:
        raise HTTPException(status_code=403, detail="Invalid Authentication Token")
    user_details = users.lookup(user_hash)
    return {"token": users.create_login_token(user_hash), "profile": profile, "admin": user_details.get('admin')}

@router.get("/me")
def me(*, authorization: str = Header(None)):
    user_detail = users.get_user_data_from_token(authorization)
    if not user_detail:
        raise HTTPException(status_code=403, detail="Invalid Authentication Token")
    return user_detail

@router.get("/all")
def all(*, authorization: str = Header(None)):
    user_detail = users.get_user_data_from_token(authorization)
    if not user_detail:
        raise HTTPException(status_code=403, detail="Invalid Authentication Token")
    if not user_detail.get('admin'):
        raise HTTPException(status_code=403, detail="You are not an admin")
    return users.get_all()

@router.get("/get-repos")
def repo_get(id: int, authorization: str = Header(None)):
    user_detail = users.get_user_data_from_token(authorization)
    if not user_detail:
        raise HTTPException(status_code=403, detail="Invalid Authentication Token")
    if not user_detail.get('admin'):
        raise HTTPException(status_code=403, detail="You are not an admin")
    return users.repo_get(id)

class UserRepos(BaseModel):
    id: int
    repos: List = None

@router.post("/set-repos")
def repo_grant(userrepos: UserRepos, authorization: str = Header(None)):
    user_detail = users.get_user_data_from_token(authorization)
    if not user_detail:
        raise HTTPException(status_code=403, detail="Invalid Authentication Token")
    if not user_detail.get('admin'):
        raise HTTPException(status_code=403, detail="You are not an admin")
    return users.repo_set(userrepos.id, userrepos.repos)    
