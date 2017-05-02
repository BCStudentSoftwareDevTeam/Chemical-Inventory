from application import app
from application.config import *
from application.models import *
from application.models.floorsModel import *
from application.models.roomsModel import *
from application.models.storagesModel import *
from application.logic.getAuthUser import AuthorizedUser
from application.logic.excelMaker import *
from playhouse.shortcuts import model_to_dict, dict_to_model


from flask import render_template, \
                  request, \
                  flash, \
                  redirect, \
                  url_for, \
                  jsonify

@app.route('/Report/', methods = ['GET', 'POST'])
def report():
    auth = AuthorizedUser()
    user = auth.getUser()
    userLevel = auth.userLevel()

    if userLevel == 'admin':
        if request.method == "GET":
            allBuild = getBuildings()
            print reportConfig.ReportTypes.Hazard
            return render_template("views/ReportView.html",
                                   authLevel = userLevel,
                                   config = config,
                                   reportConfig = reportConfig,
                                   allBuild = allBuild)
        else:
            data = request.form
            print data
            locData = genLocationReport(data)
            print reportConfig["ReportTypes"]["LocationBased"]["LocationQuantity"]["row_title"]
            exportExcel("Test", reportConfig["ReportTypes"]["LocationBased"]["LocationQuantity"]["row_title"], reportConfig["ReportTypes"]["LocationBased"]["LocationQuantity"]["queries"], locData)
            return redirect(url_for("report"))

@app.route('/locationData/', methods = ['GET'])
def locationData():
    locId = request.args.get('locId')
    locType = request.args.get('locType')
    print locType
    if locType == "Building":
        locObject = getFloors(locId)
        objectType = "Floor"
    elif locType == "Floor":
        locObject = getRooms(locId)
        objectType = "Room"
    elif locType == "Room":
        locObject = getStorages(locId)
        objectType = "Storage"
    locs = list()
    for loc in locObject:
        locs.append(model_to_dict(loc))
    return jsonify({'status':'OK',
                    'locObject' : locs,
                    'objectType' : objectType})
