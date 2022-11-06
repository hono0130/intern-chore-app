from fastapi import APIRouter, Depends, Form
from fastapi.security import OAuth2PasswordRequestForm

import schemas.user as user_schema
from auth import get_current_user, create_tokens, authenticate
from models.model import User
from cruds.user import update_user, create_user

router = APIRouter()

@router.post("/token", response_model=user_schema.Token)
async def signin(form: OAuth2PasswordRequestForm = Depends()):
    """
    認証
    form.usernameはformに入力されたemailのこと

    """
    user = authenticate(form.username, form.password)
    return create_tokens(user.user_id)

@router.post("/signup", response_model=None)
async def signup(user_info: user_schema.SignUpUser):
    """
    新規登録
    ユーザー名とメールアドレスとパスワードをDBに格納

    Args:
        user_info (user_schema.SignUpUser): ユーザー名、メールアドレス、パスワード
    """
    create_user(user_info)

@router.put("/user/update")
async def user_update(user_info: user_schema.UserUpdate, current_user: User = Depends(get_current_user)):
    """
    ユーザー情報の更新

    """
    update_user(current_user.user_id, user_info)