from application.models.util import *
from application.logic.sortPost import *


class Wastechemicals (Model):
    wCHEMID = PrimaryKeyField()
    wName   = CharField(null = False)
    wCasNo  = CharField(null = True)
    wFlam   = BooleanField(default = False)
    wCorr   = BooleanField(default = False)
    wTox    = BooleanField(default = False)
    wReact  = BooleanField(default = False)
    wBio    = BooleanField(default = False)
    wRadio  = BooleanField(default = False)
    wHealth = BooleanField(default = False)
    wPlist  = BooleanField(default = False)

    class Meta:
        database = getDB("inventory", "dynamic")
