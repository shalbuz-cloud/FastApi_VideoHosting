from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

from . import schemas, services

templates = Jinja2Templates(directory='templates')

router = APIRouter(tags=['auth'])


@router.get('/')
async def google_auth(request: Request):
    return templates.TemplateResponse('auth.html', {'request': request})


@router.post('/google/auth', response_model=schemas.Token)
async def google_auth(user: schemas.UserCreate):
    user_id, token = await services.google_auth(user)
    return schemas.Token(id=user_id, token=token)
