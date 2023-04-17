from application.config import *
from application.absolutepath import getAbsolutePath
from peewee import *
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

