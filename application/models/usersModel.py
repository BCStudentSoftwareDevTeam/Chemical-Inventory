from application.models.util import *
from application.logic.sortPost import *

class Users (Model):
    userId       = PrimaryKeyField()
    username     = TextField(null = False, unique = True)
    auth_level   = TextField(null = False)
    emailadd     = TextField(null = True)
    approve      = BooleanField(default = False)
    created_date = DateTimeField(null = True)
    end_date     = DateTimeField(null = True)
    reportto     = TextField(null = False)
    created_by   = TextField(null = True)
    
    class Meta:
        database = getDB("inventory", "dynamic")

def createUser(data, createdBy):
    modelData, extraData = sortPost(data, Users)
    modelData['approve'] = True
    modelData['username'] = modelData['username'].lower()
    modelData['created_by'] = createdBy
    modelData['created_date'] = datetime.date.today()
    # Peewee has a get_or_create function. Would that be more useful than putting this in a try/except?
    try:
        Users.create(**modelData)
        return(u"Success: User added successfully.", 'list-group-item list-group-item-success')
    except:
        return(u"Error: User could not be added.", 'list-group-item list-group-item-danger')