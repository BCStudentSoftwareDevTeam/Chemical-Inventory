from peewee import *
import os

# from app import login
from application.config import config

def getMySQLDB():
    if os.environ.get("USING_CONTAINER", False):
        config['db']['host'] = 'db'
    else:
        config["db"]["host"] = "localhost"
    db_cfg = config['db']
    theDB = MySQLDatabase(db_cfg['name'], host = db_cfg['host'], user = db_cfg['username'], passwd = db_cfg['password'])
    return theDB

mainDB = getMySQLDB()

class BaseModel(Model):
    class Meta:
        database = mainDB
