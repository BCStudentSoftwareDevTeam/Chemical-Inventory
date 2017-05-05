from openpyxl import Workbook
import datetime
from application import app
from application.config import *
from application.queries.locationReportQueries import *
from application.queries.hazardReportQueries import *

def exportExcel(title, row_headers, indexes, objects):
    book = Workbook()
    sheet = book.active
    sheet.title = title
    sheet.append(row_headers)
    for row in range(len(objects)):
        for col in range(len(row_headers)):
            ##Writes out each cell with the correct value, objects found in yaml
            sheet.cell(column=col+1, row=row+2, value = eval(indexes[row_headers[col].replace(" ", "_")]))
    now = datetime.datetime.now()
    report_name = title + "_" + str(now.day) + "-" + str(now.month) + "-" + str(now.year)+".xlsx"
    book.save(filename = config["export"]["path"] + report_name)
    return report_name

def genLocationReport(locData):
    """
    Returns a file of all chemicals and containers in a location
    """
    for cont in getChemInLoc(locData):
        print cont.chemId.name
    return getChemInLoc(locData)

def genHazardReport(building):
    """
    Returns the quantity of each hazard by floor in building
    """
    return 0

def genSpecialHazardList():
    """
    Returns all special hazards (Peroxide, Pressure, Toxin/Time, Req_Stabalizer)
    """
    return 0
