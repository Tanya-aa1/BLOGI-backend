from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class PostBase(BaseModel):
    title: str
    content: str
    image_url: str | None = None 

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass

class PostOut(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime | None = None
    author: UserResponse  
    class Config:
        from_attributes = True