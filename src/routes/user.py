from typing import List, Dict
from sqlalchemy import and_

from fastapi import APIRouter

from src.models.user import Users
from src.schemas.user import (
        User, UserWithID, UserCreateRegister,
        UserCreateLogin, UserGetLogin
    )  # no-qa
from src.config.db import conn

user_router = APIRouter(prefix="/users")


# get all users
@user_router.get("/")
async def get_users() -> List[UserWithID]:
    return conn.execute(Users.select()).fetchall()


# add new user
@user_router.post("/register")
async def register_user(user: UserCreateRegister) -> List[UserWithID]:
    conn.execute(Users.insert().values({
        "name": user.name,
        "email": user.email,
        "password": user.password
    }))
    conn.commit()
    return conn.execute(Users.select()).fetchall()


# add new user
@user_router.post("/login")
async def login_user(user: UserCreateLogin) -> UserGetLogin:
    logged_in_user = conn.execute(
        Users.select().where(
            and_(
                Users.c.email == user.email,
                Users.c.password == user.password
            )
        )
    ).fetchone()
    return logged_in_user


# get a users
@user_router.get("/{id}")
async def get_user(id: int) -> User:
    return conn.execute(Users.select().where(Users.c.id == id)).fetchone()


# update a user
@user_router.put("/{id}")
def update_user(id: int, user: UserCreateRegister) -> User:
    old_user = conn.execute(Users.select().where(Users.c.id == id)).fetchone()
    print("old_user", old_user)
    result = conn.execute(Users.update().where(Users.c.id == id).values(
        name=user.name if user.name else old_user.name,
        email=user.email if user.email else old_user.email,
        password=user.password if user.password else old_user.password
    ))
    conn.commit()
    print("result", result)
    return conn.execute(Users.select().where(Users.c.id == id)).fetchone()


# delete a user
@user_router.delete("/{id}")
def delete_user(id: int) -> Dict[str, User]:
    deleted_user = conn.execute(Users.select().where(
        Users.c.id == id)).fetchone()
    conn.execute(Users.delete().where(Users.c.id == id))
    conn.commit()
    return {"deleted_user": deleted_user}
