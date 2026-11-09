from fastapi import APIRouter, HTTPException, status

from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserServiceDep

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(data: UserCreate, user_service: UserServiceDep):
    try:
        return user_service.createUser(data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, user_service: UserServiceDep):
    try:
        return user_service.getUserById(user_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/", response_model=list[UserResponse])
async def list_users(user_service: UserServiceDep):
    try:
        return user_service.getUsers()
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, user_service: UserServiceDep):
    try:
        user_service.deleteUser(user_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
