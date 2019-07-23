from app import db
from typing import List
from .model import User
from .interface import UserInterface


class UserService():
    @staticmethod
    def get_all() -> List[User]:
        return User.query.all()

    @staticmethod
    def get_by_id(user_id: int) -> User:
        return User.query.get(user_id)

    @staticmethod
    def update(user: User, User_change_updates: UserInterface) -> User:
        user.update(User_change_updates)
        db.session.commit()
        return user

    @staticmethod
    def delete_by_id(user_id: int) -> List[int]:
        user = User.query.filter(User.user_id == user_id).first()
        if not user:
            return []
        db.session.delete(user)
        db.session.commit()
        return [user_id]

    @staticmethod
    def create(new_attrs: UserInterface) -> User:
        print(new_attrs)
        new_user = User(
            user_id=new_attrs['userId'],
            email=new_attrs['email'],
            password=new_attrs['password']
        )

        db.session.add(new_user)
        db.session.commit()

        return new_user
