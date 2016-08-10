from application.models.util import *

class Users (Model):
    userId = PrimaryKeyField()
    username = TextField(null = False)
    auth_level = TextField(null = False)
    emailadd = TextField(null = False)
    approve = BooleanField(default = False)
    start_date = DateTimeField(null = True)
    end_date = DateTimeField(null = True)
    reportto = TextField(null = False)
    created_by = TextField(null = True)
    
    class Meta:
        database = getDB("inventory")