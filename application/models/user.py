from application.models.util import *

class Users (Model):
    userId = PrimaryKeyField()
    username = TextField(null = False)
    auth_level = TextField(null = False)
    start_date = DateTimeField(null = False)
    report_to = TextField(null = True)
    created_by = TextField(null = False)