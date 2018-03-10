from application.models.util import *
from application.logic.sortPost import *
import  datetime

class Wastecontainers (Model):
    wID              = PrimaryKeyField()
    wQuant           = FloatField(null = False)
    wQuantUnit       = CharField(default = "")
    wState           = CharField(default = "")
    wStorageDate     = DateTimeField(default = datetime.date.today)
    wProf            = CharField(default = "")
    wCourse          = CharField(default = "")
    wDept            = CharField(default = "")
    wBldg            = CharField(default = "")
    wRoom            = CharField(default = "")
    wSemester        = CharField(default = "")

    class Meta:
        database = getDB("inventory", "dynamic")
