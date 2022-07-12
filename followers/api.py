from typing import List

from fastapi import APIRouter, Depends

from user.auth import current_active_user
from user.models import User
from .schemas import FollowerCreate, FollowerList
from .models import Follower

router = APIRouter(prefix='/followers', tags=['followers'])


@router.post('/', status_code=201)
async def add_follower(
        schema: FollowerCreate, user: User = Depends(current_active_user)
):
    host = await User.objects.get(id=schema.user)
    return await Follower.objects.create(subsciber=user.dict(), user=host)


@router.get('/', response_model=List[FollowerList])
async def my_list_following(user: User = Depends(current_active_user)):
    return await Follower.objects.select_related(['user', 'subscriber'])\
        .get_or_none(subscriber=user)


@router.get('/me', response_model=List[FollowerList])
async def my_list_follower(user: User = Depends(current_active_user)):
    return await Follower.objects.select_related('user')\
        .filter(user=user).all()
