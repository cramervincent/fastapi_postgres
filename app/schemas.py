from typing import List, Union, Optional
from pydantic import BaseModel


class User(BaseModel):
    is_active: bool
    password: str
    email: str
    fullname:str
    role:str
    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    is_active: bool | None = None
    password: str | None = None
    email: str | None = None
    fullname:str | None = None
    role:str | None = None
    class Config:
        orm_mode = True

class ResponseUser(BaseModel):
    id:int | None = None
    fullname: str | None = None
    is_active: bool | None = None
    email: str | None = None
    role:str | None = None
    class Config:
        orm_mode = True


class Login(BaseModel):
    email:str
    password:str