from fastapi import APIRouter, Depends, Security
from app.api.v1.auth.dependencies import get_current_user
from app.models.user import User
from app.schemas.user import UserResponse

router = APIRouter()


@router.get("/me", response_model=UserResponse)
async def read_users_me(current_user: User = Security(get_current_user, scopes=["user:read"])):
    return current_user