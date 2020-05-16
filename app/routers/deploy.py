from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel
from ..services import util, users, deploy

router = APIRouter()

@router.get("/status")
def get_status(repository: str, authorization: str = Header(None)):
    user_detail = users.get_user_data_from_token(authorization)
    if not user_detail:
        raise HTTPException(status_code=403, detail="Invalid Authentication Token")
    return deploy.get_status(repository)

class Release(BaseModel):
    repository: str
    image: str

@router.post("/release")
def set_release(release: Release, authorization: str = Header(None)):
    user_detail = users.get_user_data_from_token(authorization)
    if not user_detail:
        raise HTTPException(status_code=403, detail="Invalid Authentication Token")
    if not deploy.set_release(release):
        return False
    return True

@router.get("/instance")
def instance(id: str):
    return deploy.instance(id)

class RepoConfig(BaseModel):
    repo: str
    config: str

@router.post("/set-config")
def set_config(rc: RepoConfig, authorization: str = Header(None)):
    user_detail = users.get_user_data_from_token(authorization)
    if not user_detail:
        raise HTTPException(status_code=403, detail="Invalid Authentication Token")
    if not deploy.set_config(rc.repo, rc.config):
        return False
    return True
