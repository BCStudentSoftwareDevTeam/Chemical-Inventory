from application import app
from peewee import *
from config import *

# PRAGMAs define how SQLite should behave.
# busy_timeout says that, if the DB is locked, that the
#   application should continue to retry for 100ms.
# journal_mode of "WAL" means "write-ahead logging",
#   which is a fancy database performance/safety thing that
#   requires more explanation than this comment can afford.
#
# threadlocals says that each thread should have its own
# connection object, as opposed to sharing one object globally.
theDB = SqliteDatabase ( config.databases.mess.filename,
                      pragmas = ( ('busy_timeout', 100),
                                  ('journal_mode', 'WAL')
                                ),
                      threadlocals = True)

class Mess (Model):
  mid     = PrimaryKeyField()
  id      = TextField()
  data    = TextField()
  size    = IntegerField()

  class Meta:
    database = theDB

# For Database setup
# Make sure to list all the model classes defined above.
models = [Mess]
