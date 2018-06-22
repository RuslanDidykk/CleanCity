# coding=utf-8
from database.DatabaseManager import DataBaseManager
from project.config import allowed_characters_for_password
from project.config import allowed_characters_for_username
from project.config import max_len_password
from project.config import max_len_username
from project.config import min_len_password
from project.config import min_len_username


class CheckManager():

    def __init__(self):
        self.db = DataBaseManager()

    def checkUserName(self, username):
        if username:
            return True
        else:
            return False

    def checkLoginData(self, password, userData):
        if password == userData.password:
            return True
        else:
            pass

    def checkCorrectionLoginData(self, username, password):
        if len(username) < min_len_username or len(username) > max_len_username:
            return False
        if len(password) < min_len_password or len(password) > max_len_password:
            return False

        for char in username:
            if char not in allowed_characters_for_username:
                return False

        for char in password:
            if char not in allowed_characters_for_password:
                return False

        return True