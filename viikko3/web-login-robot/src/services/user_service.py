import re

from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password or not password_confirmation:
            raise UserInputError("Username, password and password confirmation are required")
        elif password != password_confirmation:
            raise UserInputError("Password confirmation doesn't match password")
        elif re.match("^[a-z]{3,}$", username) is None:
            raise UserInputError("Username is too short or contains characters other than lowercase letters")
        elif re.match("^[a-zA-Z]+$", password) or len(password) < 8:
            raise UserInputError("Password is too short or contains only lowercase letters")


user_service = UserService()
