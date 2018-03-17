# coding=utf-8
from database.DatabaseModel import Users
from database.DatabaseManager import DataBaseManager
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy import update
from sqlalchemy.orm import sessionmaker
from database.config import database_uri
from config import allowed_characters_for_username
from config import allowed_characters_for_password
from config import min_len_username
from config import min_len_password
from config import max_len_username
from config import max_len_password


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


# if __name__ == '__main__':
#     CheckManager().checkUser('ruslan', 'didyk')


    # def selectALl(self):
    #     with self.getConnection() as connection:
    #         try:
    #             data = connection.query(Users).filter(Project.project_id == 1).all()
    #             #возвращает список обьектов
    #
    #             for user in data:
    #                 print user.name
    #         except Exception as e:
    #             print e

# db = DataBaseManager()
# db.insert_urls()
# db.addCar(model='BMW')
# db.updateUser(1,2)
# db.selectALl()