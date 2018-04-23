# coding=utf-8
from database.DatabaseModel import Users, Sprzet

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

    def addUser(self, data):
        with self.getConnection() as connection:
            try:
                project = Users(user_name=data['username'],
                                password=data['password'],
                                account_type=data['account_type'],
                                mail=data['mail'],
                                imie=data['imie'],
                                nazwisko=data['nazwisko'],
                                telefon=data['telefon'],
                                adres=data['adres'],
                                kod_pocztowy=data['kod_pocztowy'],
                                PESEL=data['pesel'])

                connection.add(project)
                connection.flush()
                connection.commit()
            except Exception as exc:
                print (exc)
                connection.rollback()
                return exc

    def addSprzet(self, nazwa, ilosc):
        with self.getConnection() as connection:
            try:
                project = Sprzet(sprzet=nazwa,
                                ilosc=ilosc)

                connection.add(project)
                connection.flush()
                connection.commit()
            except Exception as exc:
                print (exc)
                connection.rollback()
                return exc

    def editUser(self, data):
        with self.getConnection() as connection:
            try:
                smtp = update(Users).where(Users.user_name == data['username']). \
                    values(
                            password=data['password'],
                            account_type=data['account_type'],
                            mail=data['mail'],
                            imie=data['imie'],
                            nazwisko=data['nazwisko'],
                            telefon=data['telefon'],
                            adres=data['adres'],
                            kod_pocztowy=data['kod_pocztowy'],
                            PESEL=data['pesel']
                           )
                connection.execute(smtp)
                connection.commit()
            except Exception as exc:
                print(exc)
                connection.rollback()
                return exc

    def getUserData(self, username):
        with self.getConnection() as connection:
            try:
                data = connection.query(Users).filter(
                        Users.user_name == username,
                        Users.active == True).first()
                return data
            except Exception as e:
                print(e)
                return None

    def insert_not_active_status(self, username):
        with self.getConnection() as connection:
            try:
                smtp = update(Users).where(Users.user_name == username). \
                    values(active = False)
                connection.execute(smtp)
                connection.commit()
            except Exception as exc:
                print(exc)
                connection.rollback()
                return exc

    def change_ilosc_sprzetu(self, nazwa_sprzetu, new_ilosc):
        with self.getConnection() as connection:
            try:
                smtp = update(Sprzet).where(Sprzet.sprzet == nazwa_sprzetu). \
                    values(ilosc = new_ilosc)
                connection.execute(smtp)
                connection.commit()
            except Exception as exc:
                print(exc)
                connection.rollback()
                return exc

if __name__ == '__main__':
    # print(DataBaseManager().editUser(data=data))
    # print(DataBaseManager().getUserData('ruslan'))
    # print(DataBaseManager().getUserData('dmytro'))
    DataBaseManager().insert_not_active_status('kanski')
