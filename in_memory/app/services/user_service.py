from typing import Annotated

from fastapi import Depends

from app.models.user import User
from app.repository.user_repository import UserRepository
from app.schemas.user import UserCreate


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def createUser(self, data: UserCreate) -> User:
        existing = self.repository.get_by_email(data.email)

        if existing:
            raise ValueError("User with this email already exists")
        user = User(id=0, email=data.email, name=data.name, password=data.password)
        return self.repository.create(user)

    def getUsers(self) -> list[User]:
        return self.repository.get_all()

    def getUserById(self, id: int) -> User | None:
        return self.repository.get_by_id(id)

    def deleteUser(self, id: int) -> bool:
        return self.repository.delete(id)


repository = UserRepository()


def get_user_service() -> UserService:
    return UserService(repository)


UserServiceDep = Annotated[UserService, Depends(get_user_service)]