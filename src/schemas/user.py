from pydantic import BaseModel


class User(BaseModel):
    name: str = ""
    email: str = ""


class UserCreateLogin(BaseModel):
    email: str
    password: str


class UserCreateRegister(User):
    password: str


class UserUpdate(User):
    password: str = ""


class UserGetLogin(User):
    id: int


class UserWithID(User):
    id: int
