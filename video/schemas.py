from pydantic import BaseModel

from user.schemas import UserOut


class User(BaseModel):
    id: int
    username: str


class UploadVideo(BaseModel):
    title: str
    description: str


class GetListVideo(BaseModel):
    id: int
    title: str
    description: str


class GetVideo(GetListVideo):
    user: UserOut


class Message(BaseModel):
    message: str
