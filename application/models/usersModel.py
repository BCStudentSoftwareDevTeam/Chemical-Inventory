from application.models.util import *

class Users (Model):
    userId = PrimaryKeyField()
    username = TextField(null = False)
    auth_level = TextField(default = "student")
    emailadd = TextField(null = False)
    approve = BooleanField(default = False)
    start_date = DateTimeField(null = False)
    reportto = TextField(null = False)
    created_by = TextField(null = True)
    
    class Meta:
        database = getDB("inventory")