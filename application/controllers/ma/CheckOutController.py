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
    jsonify, \
    url_for
    
# PURPOSE: Check out a container
@app.route('/ma/checkOut/', methods=['GET', 'POST'])
@require_role('admin')
def maCheckOut():
    storageList = Storages.select()
    buildingList = Buildings.select()
    if request.method == "POST":
        data = request.form
        cont = Containers.get(Containers.barcodeId == data['barcodeId'])
        Histories.create(movedFrom = cont.storageId,
                        movedTo = data['storageId'],
                        containerId = cont.barcodeId,
                        modUser = "CheckOutTest",
                        action = "Checked Out",
                        pastQuantity = "%s %s" %(cont.currentQuantity, cont.currentQuantityUnit))
        cont.storageId = data['storageId']
        cont.checkedOut = True
        cont.checkOutReason = data['forClass']
        cont.forProf = data['forProf']
        cont.checkedOutBy = data['user']
        cont.save()
    return render_template("views/ma/CheckOutView.html",
                           config = config,
                           contConfig = contConfig,
                           container = None, #container = None is needed as a placeholder for the page before the barcode is entered.
                           buildingList = buildingList,
                           storageList = storageList,
                           pageConfig = checkOutConfig)