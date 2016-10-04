from application.config import *
from peewee import *

def getDB (dbName, dbType):
  dbPath = config.databases[dbType][dbName].filename
  # print "DB Name: {0}\nDB Path: {1}".format(dbName, dbPath)
  theDB = SqliteDatabase (dbPath,
                          pragmas = ( ('busy_timeout',  100),
                                      ('journal_mode', 'WAL')
                                  ),
                          threadlocals = True)
  config.databases[dbType][dbName].theDB = theDB
  return theDB
  
