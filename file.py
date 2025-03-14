from dataclasses import dataclass
# CRUD: Create, Read, Update, Delete


@dataclass(frozen=False)
class User:
    email: str
    password: str

class File:
    def __init__(self, path: str):
        self.__path_file = path
    
    @classmethod
    def new(cls, *, path: str):
        return cls(path=path)

    def read(self) -> list[User]:
        users: list[User] = []

        with open(self.__path_file, "r") as file:
            # read file -> list of string for each line
            data = file.readlines()

            # loop every string lines
            for index in range(len(data)):
                # split email and password
                # from "email,password" -> ["email", "password\n"]
                current_user = data[index].split(",")
                # delete "\n" since "\n" stays behide password, we have to "\n" from password
                # by replace "\n" with ""; "\n" -> ""

                # create new user obj (real case would be dictionary)
                new_user = User(email=current_user[0], password=current_user[1].replace("\n", ""))

                # append to list
                users.append(new_user)

        return users
    
    # void append()
    def append(self, email: str, password: str) -> None:
        # email,password
        new_user = email + "," + password
        # read file
        file = open(self.__path_file, "a")
        # write new line
        file.writelines("\n")
        # write user data
        file.writelines(new_user)
        # close file
        file.close()




