from application import app
from application.models.chemicalsModel import *
from application.models.containersModel import *
from application.models.storagesModel import *
from application.models.buildingsModel import *
from application.models.historiesModel import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    json as simplejson, \
    url_for

# PURPOSE: CheckIn a container
@app.route('/sa/CheckIn/', methods = ['GET', 'POST'])
@require_role('admin')
def saCheckIn():
    storageList = Storages.select()
    buildingList = Buildings.select()
    if request.method == "POST":
        data = request.form
        cont = Containers.get(Containers.barcodeId == data['barcodeId'])
        Histories.create(movedFrom = cont.storageId,
                       movedTo = data['storageId'],
                       containerId = cont.barcodeId,
                       modUser = "CheckInTest",
                       pastQuantity = "%s %s" %(cont.currentQuantity, cont.currentQuantityUnit))
        cont.storageId = data['storageId']
        cont.currentQuantity = data['currentQuantity']
        cont.currentQuantityUnit = data['currentQuantityUnit']
        cont.checkedOut = False
        cont.checkOutReason =''
        cont.forProf = ''
        cont.checkedOutBy = ''
        cont.save()
    return render_template("views/sa/CheckInView.html",
                           config = config,
                           contConfig = contConfig,
                           container = None, #container = None is needed as a placeholder for the page before the barcode is entered.
                           buildingList = buildingList,
                           storageList = storageList,
                           pageConfig = checkInConfig)