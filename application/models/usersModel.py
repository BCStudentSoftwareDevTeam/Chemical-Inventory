from application.models.util import *

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
