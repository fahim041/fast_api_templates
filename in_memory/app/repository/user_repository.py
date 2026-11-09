from app.models.user import User


class UserRepository:
    def __init__(self) -> None:
        self.users: dict[int, User] = {}
        self.next_id = 1

    def create(self, user: User) -> User:
        user.id = self.next_id
        self.users[user.id] = user
        self.next_id += 1
        return user

    def get_all(self) -> list[User]:
        return list(self.users.values())

    def get_by_id(self, id: int) -> User | None:
        return self.users.get(id, None)

    def get_by_email(self, email: str) -> User | None:
        for user in self.users.values():
            if user.email == email:
                return user
        return None

    def delete(self, id: int) -> bool:
        return self.users.pop(id, None) is not None
