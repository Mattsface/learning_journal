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
    created = Column(DateTime, default=func.now())
    edited = Column(DateTime, default=func.now(), onupdate=func.now())

    @classmethod
    def by_id(cls, entryid, session=None):
        if session is None:
            session = DBSession
        return session.query(cls).filter(cls.id==entryid).first()

    @classmethod
    def all(cls, session=None):
        if session is None:
            session = DBSession
        return session.query(cls).order_by(sa.desc(cls.created)).all()


Index('my_index', MyModel.name, unique=True, mysql_length=255)
