from typing import Self
from file import File, User

DATABASE_PATH = "./database.txt"

class Authentication:
    def __init__(self, file: File):
        self.file: File = file
    
    @classmethod
    def new(cls, *, file: File) -> "Authentication":
        return cls(file=file)
    
    def get_data(self) -> list[User]:
        return self.file.read()
    
    # private
    def __find_user_from_email(self, email: str) -> User | None:
        users: list[User] = self.file.read()

        for index in range(len(users)):
            current_user = users[index]
            user_email = current_user.email
            if user_email == email:
                return current_user
        # null
        return None

    # public
    def sign_in(self: Self, email: str, password: str) -> dict[str, str]:
        user = self.__find_user_from_email(email=email)
        # if user does not exist 
        if not user:
            return None

        # check password
        if user.password != password:
            return None

        # convert from obj to class
        return user.__dict__

    # public
    def sign_up(self: Self, email: str, password: str) -> bool:
        has_user = self.__find_user_from_email(email=email)
        if has_user:
            return False
        
        if len(password) < 8:
            return False

        self.file.append(email=email, password=password)
        return True


file = File(path=DATABASE_PATH)
auth = Authentication.new(file=file)
user = auth.sign_in(email="email", password="password")