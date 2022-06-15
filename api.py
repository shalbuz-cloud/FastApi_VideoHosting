from fastapi import APIRouter, UploadFile, File, Form, BackgroundTasks
from fastapi.responses import StreamingResponse

from schemas import GetVideo, Message
from models import Video, User
from services import save_video

router = APIRouter()


@router.post("/")
async def create_video(
        background_tasks: BackgroundTasks,  # Фоновая загрузка
        title: str = Form(...),
        description: str = Form(...),
        file: UploadFile = File(...)
) -> Video:
    user = await User.objects.first()  # TODO: Выбор пользователя БД
    return await save_video(
        user, file, title, description, background_tasks
    )


@router.get(
    '/video/{video_pk}',
    response_model=GetVideo,
    responses={404: {'model': Message}}
)
async def get_video(video_pk: int):
    file = await Video.objects.select_related('user').get(pk=video_pk)
    file_like = open(file.dict().get('file'), mode='rb')
    return StreamingResponse(file_like, media_type='video/mp4')
