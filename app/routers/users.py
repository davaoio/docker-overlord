from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel
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
    user_id = users.find_or_create_user(f"github||{profile.get('id')}", profile)
    util.logger.warning(f"GitHub Account Logged In: {user_id} ({profile.get('id')})")
    if not user_id:
        raise HTTPException(status_code=403, detail="Invalid Authentication Token")
    return {"token": users.create_login_token(user_id), "profile": profile}

@router.get("/me")
def me(*, authorization: str = Header(None)):
    user_detail = users.get_user_data_from_token(authorization)
    if not user_detail:
        raise HTTPException(status_code=403, detail="Invalid Authentication Token")
    return user_detail
