from typing import Optional
import datetime

from pydantic import BaseModel, Field

class UserBase(BaseModel):
    email: str = Field(regex=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", example="test@example.com")
    password: str = Field(regex=r'\A[a-z\d]{8,100}\Z(?i)')

class SignUpUser(UserBase):
    username: str

class UserUpdate(SignUpUser):
    layout: Optional[str] = Field(None)
    gender: Optional[str] = Field(None)
    birthday: Optional[datetime.date] = Field(None)
    user_id: int
    class config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
