from fastapi.requests import Request

from user.schemas import UserDB


def on_after_register(user: UserDB, request: Request):
    print('User %s has registered.' % user.id)
