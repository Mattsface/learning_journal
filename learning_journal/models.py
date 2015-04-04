from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
    func
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

from datetime import datetime

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Text(length=255, convert_unicode=True), unique=True, nullable=False)
    body = Column(Text(length=None, convert_unicode=True))
    created = Column(DateTime, default=func.now())
    edited = Column(DateTime, onupdate=func.utc_timestamp())





Index('my_index', MyModel.name, unique=True, mysql_length=255)
