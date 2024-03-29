from fastapi import FastAPI

from video.api import router as video_router
from user.api import router as user_router
from followers.api import router as follower_router
from db import database, metadata, engine

app = FastAPI()

metadata.create_all(engine)
app.state.database = database


@app.on_event('startup')
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event('shutdown')
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


app.include_router(user_router)
app.include_router(video_router)
app.include_router(follower_router)
