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

def create_DB():
    engine = create_engine(database_uri)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    create_DB()