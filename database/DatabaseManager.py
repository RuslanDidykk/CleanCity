# coding=utf-8
from time import strftime, gmtime

import dateparser

from database.DatabaseModel import Users, Sprzet, Pojazd, Harmonogram, Orders

from contextlib import contextmanager
from sqlalchemy import create_engine, cast, Date, desc
from sqlalchemy import update
from sqlalchemy.orm import sessionmaker
from database.config import database_uri
import datetime

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

    def add_item_to_harmongram(self, data):
        with self.getConnection() as connection:
            try:
                project = Harmonogram(klient_nazwa=data['klient_nazwa'],
                                pracownik=data['pracownik'],
                                pojazd=data['pojazd'],
                                ulica=data['ulica'],
                                date=data['date'],
                                sprzet=data['sprzet'],
                                sprzet_ilosc=data['sprzet_ilosc'])
                connection.add(project)
                connection.flush()
                connection.commit()
            except Exception as exc:
                print (exc)
                connection.rollback()
                return exc

    def edit_status_pojazd(self, data):
        with self.getConnection() as connection:
            try:
                smtp = update(Pojazd).where(Pojazd.numer == data['pojazd']). \
                    values(
                        status=data['status']
                           )
                connection.execute(smtp)
                connection.commit()
            except Exception as exc:
                print(exc)
                connection.rollback()
                return exc

    def delete_wyjazd(self, id):
        with self.getConnection() as connection:
            try:
                smtp = connection.query(Harmonogram).filter(Harmonogram.id == int(id)).delete()
                connection.commit()
            except Exception as exc:
                print(exc)
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

    def add_order(self, klient_username, ulicy):
        with self.getConnection() as connection:
            try:
                project = Orders(klient_username=klient_username,
                                 order_description=ulicy,
                                 order_date=datetime.date.today())

                connection.add(project)
                connection.flush()
                connection.commit()
            except Exception as exc:
                print (exc)
                connection.rollback()
                return str(exc)

    def add_pojazd(self, nazwa, numer):
        with self.getConnection() as connection:
            try:
                project = Pojazd(nazwa=nazwa,
                                numer=numer)
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

    def get_all_pracownikow(self):
        with self.getConnection() as connection:
            try:
                data = connection.query(Users).filter(
                        Users.active == True,
                        Users.account_type == 'user').all()

                return data
            except Exception as e:
                print(e)
                return None

    def get_all_klientow(self):
        with self.getConnection() as connection:
            try:
                data = connection.query(Users).filter(
                        Users.active == True,
                        Users.account_type == 'klient').all()

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

    def get_sprzet_info(self, nazwa_sprzetu):
        with self.getConnection() as connection:
            try:
                data = connection.query(Sprzet).filter(
                        Sprzet.sprzet == nazwa_sprzetu).first()
                return data
            except Exception as e:
                print(e)
                return None

    def get_all_sprzet(self):
        with self.getConnection() as connection:
            try:
                data = connection.query(Sprzet).all()
                return data
            except Exception as e:
                print(e)
                return None

    def get_all_orders(self):
        with self.getConnection() as connection:
            try:
                data = connection.query(Orders).all()
                return data
            except Exception as e:
                print(e)
                return None

    # def get_all_pojazd(self):
    #     with self.getConnection() as connection:
    #         try:
    #             data = connection.query(Pojazd).filter(
    #                     Sprzet.sprzet == nazwa_sprzetu).all()
    #             return data
    #         except Exception as e:
    #             print(e)
    #             return None

    def get_all_pojazd(self):
        with self.getConnection() as connection:
            try:
                data = connection.query(Pojazd).all()
                return data
            except Exception as e:
                print(e)
                return None

    def get_all_active_pojazd(self):
        with self.getConnection() as connection:
            try:
                data = connection.query(Pojazd)\
                    .filter(Pojazd.status == 'Active').all()
                return data
            except Exception as e:
                print(e)
                return None


    def get_all_users(self):
        with self.getConnection() as connection:
            try:
                data = connection.query(Users).all()
                return data
            except Exception as e:
                print(e)
                return None


    def get_all_actual_harmonogram(self):
        with self.getConnection() as connection:
            try:
                data = connection.query(Harmonogram).filter(
                    cast(Harmonogram.date, Date) > datetime.date.today()
                ).order_by(Harmonogram.date).all()
                return data
            except Exception as e:
                print(e)
                return None

    def get_all_actual_harmonogram_for_user(self, user_name):
        with self.getConnection() as connection:
            try:
                data = connection.query(Harmonogram).filter(
                    cast(Harmonogram.date, Date) > datetime.date.today(),
                    Harmonogram.pracownik == user_name
                ).order_by(Harmonogram.date).all()
                return data
            except Exception as e:
                print(e)
                return None

    def check_person_in_harmonogram(self, pracownik, date):
        with self.getConnection() as connection:
            try:
                data = connection.query(Harmonogram).filter(
                    cast(Harmonogram.date, Date) == date,
                    Harmonogram.pracownik == pracownik
                ).first()
                return data.pracownik
            except Exception as e:
                # print(e)
                return None

    def check_ilosc_pracownikow_na_pojazdzie(self, pojazd, date):
        with self.getConnection() as connection:
            try:
                data = connection.query(Harmonogram).filter(
                    cast(Harmonogram.date, Date) == date,
                    Harmonogram.pojazd == pojazd
                ).all()
                return data
            except Exception as e:
                # print(e)
                return None

if __name__ == '__main__':
    # print(DataBaseManager().editUser(data=data))
    # print(DataBaseManager().getUserData('ruslan'))
    # print(DataBaseManager().getUserData('dmytro'))
    # DataBaseManager().insert_not_active_status('kanski')
    # date = dateparser.parse('2018-05-25')
    # temp = datetime.date.today()

    list_data = DataBaseManager().add_order('klient','ads')