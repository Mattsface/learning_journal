import datetime
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
    Unicode,
    UnicodeText,
    func
    )

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

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
    title = Column(Unicode(length=255), unique=True, nullable=False)
    body = Column(UnicodeText(), default=u'')
    created = Column(DateTime, default=datetime.datetime.utcnow)
    edited = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    @classmethod
    def by_id(cls, entryid, session=None):
        """
        return entry an entry based on its index id, if not found return None
        """
        if session is None:
            session = DBSession
        return session.query(cls).filter(cls.id==entryid).first()

    @classmethod
    def all(cls, session=None):
        """
        Return all entries by creation date
        """
        if session is None:
            session = DBSession
        return session.query(cls).order_by(sa.desc(cls.created)).all()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(Unicode(length=255), unique=True, nullable=False)
    password = Column(Unicode(), nullable=True)
    @classmethod
    def by_user(cls, username, session=None):
        """
        return entry an entry based on its index id, if not found return None
        """
        if session is None:
            session = DBSession
        return session.query(cls).filter(cls.username==username).first()



Index('my_index', MyModel.name, unique=True, mysql_length=255)
