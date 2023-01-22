from application.config import *
from application.absolutepath import getAbsolutePath
from peewee import *

# def getDB (dbName, dbType):
#   dbPath = config.databases[dbType][dbName].filename
#   dbPath = getAbsolutePath(dbPath)
#   # print "DB Name: {0}\nDB Path: {1}".format(dbName, dbPath)
#   theDB = SqliteDatabase (dbPath,
#                           pragmas = ( ('busy_timeout',  100),
#                                       ('journal_mode', 'WAL')
#                                   ),
#                           threadlocals = True)
#   config.databases[dbType][dbName].theDB = theDB
#   return theDB

import yaml
from application.absolutepath import getAbsolutePath
from peewee import SqliteDatabase

with open('config/config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

def getDB(dbName, dbType):
    dbPath = config['databases'][dbType][dbName]['filename']
    dbPath = getAbsolutePath(dbPath)
    theDB = SqliteDatabase(dbPath,
                           pragmas=(('busy_timeout', 100),
                                    ('journal_mode', 'WAL')
                                    ),
                           threadlocals=True)
    config['databases'][dbType][dbName]['theDB'] = theDB
    return theDB

