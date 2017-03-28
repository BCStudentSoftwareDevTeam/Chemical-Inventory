from openpyxl import Workbook
import datetime
from application import app
from application.config import *
from application.models.chemicalsModel import *
from application.models.containersModel import *
from application.models.roomsModel import *
from application.models.storagesModel import *
from application.models.buildingsModel import *
from application.models.historiesModel import *

def exportExcel(title):
    book = Workbook()
    sheet = book.active
    sheet.title = title
    sheet.append(['Row1', 'Row2', 'Row3'])
    book.save(filename = config["export"]["path"])

def locationReport():
    """
    Returns a file of all chemicals and containers in a location
    """
    return 0

def hazardReport(building):
    """
    Returns the quantity of each hazard by floor in building
    """
    return 0

def specialHazardList():
    """
    Returns all special hazards (Peroxide, Pressure, Toxin/Time, Req_Stabalizer)
    """
    return 0
