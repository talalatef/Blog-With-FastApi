from pydantic import BaseModel
from typing import List

class BlogPost(BaseModel):
    title: str
    content: str
    user_id: int

class GetBlogCreator(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

class GetBlog(BaseModel):
    id: int
    title: str
    content: str
    creator: GetBlogCreator

    class Config:
        orm_mode = True

class GetUserBlog(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None

class GetUser(BaseModel):
    id: int
    name: str
    email: str
    blogs: List[GetUserBlog]

    class Config:
        orm_mode = True
