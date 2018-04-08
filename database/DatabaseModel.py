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

class Sprzet(Base):
    __tablename__ = 'sprzet'
    id = Column(Integer, primary_key=True)
    sprzet = Column(String(60), unique=True)
    ilosc = Column(Integer)


def create_DB():
    engine = create_engine(database_uri)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    create_DB()