from application import app
from application.models.batchModel import *
from application.models.mainModel import * 
from application.models.locatesModel import *
from application.models.chemicalsModel import *
from application.config import *


from flask import render_template, \
        request, \
        jsonify

@app.route('/ma/migrateChem/', methods = ['GET', 'POST'])
def maMigrateChem():

    containerObj = None
    #locdict = Batch.select().dicts().get() This was used for datamodel testing
    if request.method == "POST":
            #Gets container from old DB by input barcode whether lower or upper case
            try:
               containerObj = Batch.select().join(Main, on =(Batch.NameRaw_id == Main.NameSorted)).join(Locates, on=(Batch.Id_id == Locates.Location)).where((Batch.UniqueContainerID == request.form['barcodeID'])|(Batch.UniqueContainerID == request.form['barcodeID'].upper())).get()
            except:
                pass
            #Checks if chemical already in system
            try:
                ###########You left off here. You are checking if chemical exists is both systems##
                containerObj.IsSupplyItem
                
                
    return render_template("views/ma/MigrateChem.html",
				    container = containerObj,
                                    config = config)
