"""
Write a scenario where a `UserAuthentication` interface contains `login()` and `logout()` methods, 
and it is implemented by `GoogleAuth` and `FacebookAuth` classes.
"""

from abc import ABC, abstractmethod

class UserAuthentication(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

class GoogleAuth(UserAuthentication):
    def login(self):
        print("Logged into Google")

    def logout(self):
        print("Logged out of Google")
        
class FacebookAuth(UserAuthentication):
    def login(self):
        print("Logged into Facebook")

    def logout(self):
        print("Logged out of Facebook")


def main():
    google = GoogleAuth()
    google.login()
    google.logout()

    fb = FacebookAuth()
    fb.login()
    fb.logout()


main()