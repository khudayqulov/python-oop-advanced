"""Task 06 — Registration with classmethod and staticmethod."""

import re


class User:
    user_count = 0

    def __init__(self, username, email, password):
        if not isinstance(username, str) or not username.strip():
            raise ValueError("Username cannot be empty")
        if not self.validate_email(email):
            raise ValueError("Invalid email address")
        if not isinstance(password, str) or not password:
            raise ValueError("Password cannot be empty")
        self.username = username.strip()
        self.email = email
        self.password = password  # Demo only; use password hashing in real apps.
        User.user_count += 1

    def get_profile(self):
        return {"username": self.username, "email": self.email}

    @classmethod
    def get_user_count(cls):
        return cls.user_count

    @staticmethod
    def validate_email(email):
        return (isinstance(email, str)
                and re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email) is not None)

    @classmethod
    def create_user(cls, data):
        if not isinstance(data, dict):
            raise TypeError("User data must be a dictionary")
        return cls(data["username"], data["email"], data["password"])


def demo():
    users = [
        User.create_user({
            "username": "ali", "email": "ali@example.com", "password": "pass1"
        }),
        User("vali", "vali@example.com", "pass2"),
        User("sardor", "sardor@example.com", "pass3"),
    ]
    for user in users:
        print(user.get_profile())
    print("Users created:", User.get_user_count())


if __name__ == "__main__":
    demo()
