# coding=utf-8
from database.DatabaseModel import Users

from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy import update
from sqlalchemy.orm import sessionmaker
from database.config import database_uri

class DataBaseManager():
    def __init__(self):
        self.pool_connetcion = self.poolConnect()

    def poolConnect(self):
        engine = create_engine(database_uri)
        return engine

    @contextmanager
    def getConnection(self):
        self.con = self.pool_connetcion.connect()
        DBSession = sessionmaker(bind=self.con)
        session = DBSession()
        try:
            yield session
        finally:
            session.close()
            self.con.close()

    def addUser(self, username, password, account_type):
        with self.getConnection() as connection:
            try:
                project = Users(user_name=username,
                                password=password,
                                account_type=account_type)
                connection.add(project)
                connection.flush()
                connection.commit()
            except Exception as exc:
                print (exc)
                connection.rollback()

    def getUserData(self, username):
        with self.getConnection() as connection:
            try:
                data = connection.query(Users).filter(
                        Users.user_name == username).first()
                return data
            except Exception as e:
                print(e)
                return Exception

if __name__ == '__main__':
    print(DataBaseManager().getUserData(username="ruslan"))
