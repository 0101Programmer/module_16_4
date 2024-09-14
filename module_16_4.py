from typing import Annotated, List
from fastapi import FastAPI, Path, HTTPException, Body
from pydantic import BaseModel

app = FastAPI()

# python -m uvicorn module_16_4:app

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def get_all_users() -> list:
    return users


@app.post('/users/{username}/{age}')
async def new_user(user: User, username: str, age: int):
    if len(users) == 0:
        user.id = 1
        user.username = username
        user.age = age
        users.append(user)
        return user
    else:
        user.id = len(users) + 1
        user.username = username
        user.age = age
        users.append(user)
        return user


@app.put('/users/{user_id}/{username}/{age}')
async def upd_user(user_id: int, username, age):
    for usr in users:
        if user_id == usr.id:
            usr.username = username
            usr.age = age
            return usr
    else:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def del_user(user_id: int):
    for usr in users:
        if user_id == usr.id:
            users.remove(usr)
            return usr
    else:
        raise HTTPException(status_code=404, detail='User was not found')
