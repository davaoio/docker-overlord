from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel
from ..services import util, users, aws

router = APIRouter()

@router.get("/ecr")
def get_ecr(*, authorization: str = Header(None)):
    user_detail = users.get_user_data_from_token(authorization)
    if not user_detail:
        raise HTTPException(status_code=403, detail="Invalid Authentication Token")
    return aws.get_ecr()

"""
@router.post("/add")
def add(message: Message, authorization: str = Header(None)):
    user_id = util.token_to_userid(authorization)
    if not user_id:
        raise HTTPException(status_code=403, detail="Invalid Authentication Token")
    response = messages.add(user_id, message.text)
    return {"msg": response}
"""