from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def sign_in(self):
        pass

    def details(self, name):
        print(f"User {name}")
        return "Hello"

class NormalUser(User):
    def login(self):
        print("normal user login")

    def sign_in(self):
        print("normal user signin")

class Admin(User):
    def login(self):
        print("Admin login")
    def sign_in(self):
        print("admin signin")

    def details(self, name):
        print(f"Admin {name}")
        return "Hello"


n = NormalUser()
n.login()
print(n.details("Hari"))


a = Admin()
a.login()
print(a.details("Boss"))


