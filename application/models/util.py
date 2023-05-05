from application.config import config 
from application.absolutepath import getAbsolutePath
from peewee import SqliteDatabase

def getDB (dbName, dbType):
  dbPath = getAbsolutePath(config['databases'][dbType][dbName]['filename'])
  # print "DB Name: {0}\nDB Path: {1}".format(dbName, dbPath)
  theDB = SqliteDatabase (dbPath,
                          pragmas = ( ('busy_timeout',  100),
                                      ('journal_mode', 'WAL')),)
  config['databases'][dbType][dbName]['theDB'] = theDB
  return theDB

from peewee import *
