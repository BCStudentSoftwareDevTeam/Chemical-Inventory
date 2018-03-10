from application.models.util import *
from application.logic.sortPost import *
from application.models.wasteContainersModel import Wastecontainers
from application.models.wasteChemicalsModel import Wastechemicals

class Wastecontents (Model):
    wCHEMID      =  PrimaryKeyField()
    wID          =  ForeignKeyField(Wastecontainers, related_name = 'container')
    wCHEMID      =  ForeignKeyField(Wastechemicals, related_name = 'chemical')
    rmWaste      =  BooleanField(default = False)

    class Meta:
        database = getDB("inventory", "dynamic")
