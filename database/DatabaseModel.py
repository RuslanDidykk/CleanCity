from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, BOOLEAN, JSON, TIMESTAMP, FLOAT, ARRAY
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from sqlalchemy import Integer
from sqlalchemy import BOOLEAN
from sqlalchemy import String

from database.config import database_uri


Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(20), unique=True)
    password = Column(String(20))
    account_type = Column(String(15))
    mail = Column(String(30), unique=True)
    imie = Column(String(30))
    nazwisko = Column(String(30))
    telefon = Column(Integer)
    adres = Column(String(100))
    kod_pocztowy = Column(String(30))
    PESEL = Column(Integer, unique=True)
    active = Column(BOOLEAN, default=True)

class Sprzet(Base):
    __tablename__ = 'sprzet'
    id = Column(Integer, primary_key=True)
    sprzet = Column(String(60), unique=True)
    ilosc = Column(Integer)

class Pojazd(Base):
    __tablename__ = 'pojazd'
    id = Column(Integer, primary_key=True)
    numer = Column(String(20), unique=True)
    nazwa = Column(String(100))
    status = Column(String(100))

class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    klient_username = Column(String(500))
    order_description = Column(String(500))
    order_date = Column(DateTime)

class Harmonogram(Base):
    __tablename__ = 'harmonogram'
    id = Column(Integer, primary_key=True)
    klient_nazwa = Column(String(200))
    ulica = Column(String(200))
    pracownik = Column(String(200))
    pojazd = Column(String(200))
    date = Column(DateTime)
    sprzet = Column(String(1000))
    sprzet_ilosc = Column(Integer)


def create_DB():
    engine = create_engine(database_uri)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    create_DB()