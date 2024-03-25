from typing import Annotated

from fastapi import APIRouter, Depends, Path

from dependency_injection import dependency_injector
from service.user.user_service import UserServiceABC
from domain.user.dto.user_dto import UserDTO

__tags = ["user"]
user_router = APIRouter(tags=__tags)


@user_router.get("/user/{user_id}", response_model=UserDTO)
async def get_user_with_user_id(
        user_id: Annotated[int, Path(title="user_id")],
        user_service: Annotated[type(UserServiceABC), Depends(dependency_injector.get_user_service)]
) -> UserDTO:
    user = await user_service.get_user_with_user_id(user_id)

    return user
