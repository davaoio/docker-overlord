from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel
from ..services import util, users, aws

router = APIRouter()

@router.get("/ecr")
def get_ecr(*, authorization: str = Header(None)):
    user_detail = users.get_user_data_from_token(authorization)
    if not user_detail:
        raise HTTPException(status_code=403, detail="Invalid Authentication Token")
    return aws.ecr_get_all()

@router.get("/ecr/details")
def get_ecr_details(repository: str):
    # TODO: Put in authentication
    return aws.ecr_get_details(repository)

@router.get("/ecr/get-images")
def get_images(repository: str, authorization: str = Header(None)):
    user_detail = users.get_user_data_from_token(authorization)
    if not user_detail:
        raise HTTPException(status_code=403, detail="Invalid Authentication Token")
    return aws.ecr_get_images(repository)    

