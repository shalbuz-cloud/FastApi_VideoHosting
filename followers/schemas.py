from pydantic import BaseModel

from user.schemas import UserOut


class FollowerCreate(BaseModel):
    user: str


class FollowerList(FollowerCreate):
    user: UserOut
    subscriber: UserOut
