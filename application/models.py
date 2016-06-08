from application import app
from playhouse.apsw_ext import APSWDatabase
# from playhouse.shortcuts import RetryOperationalError
from peewee import *
from config import *

theDB = APSWDatabase( config.database.filename, 
                      pragmas = (('busy_timeout', 100), ('journal_mode', 'WAL')),
                      threadlocals = True)
                      
# theDB = SqliteDatabase(config.database.filename)

# For Database setup
models = ['Mess']

class Mess (Model):
  mid     = PrimaryKeyField()
  id      = TextField()
  data    = TextField()
  size    = IntegerField()
  
  class Meta:
    database = theDB
