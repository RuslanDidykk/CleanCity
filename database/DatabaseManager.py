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

    def addUser(self, id, user_name, password):
        with self.getConnection() as connection:
            try:
                project = Users(id=id,
                                user_name=user_name,
                                password=password)
                connection.add(project)
                connection.flush()
                connection.commit()
            except Exception as exc:
                print (exc)
                connection.rollback()


    # def selectALl(self):
    #     with self.getConnection() as connection:
    #         try:
    #             data = connection.query(Project).filter(Project.project_id == 1).all()
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