#!/usr/bin/env python
from pyramid.paster import get_appsettings
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker


config = 'development.ini'
settings = get_appsettings(config)
engine = engine_from_config(settings, 'sqlalchemy.')
Session = sessionmaker(bind=engine)
session = Session()


# Import models
from learning_journal.models import MyModel
from learning_journal.models import Entry

print session.query(MyModel).all()

# lets create a couple Entry

#entry1 = Entry(title='First', body='Some text and stuff')
#entry2 = Entry(title='Second', body='Some text and stuff')
#session.add(entry1)
#session.add(entry2)
#session.comm

print Entry().by_id(2, session)





