from application import app
from application.models.staticModels.batchModel import *
from application.models.staticModels.mainModel import * 
from application.models.staticModels.locatesModel import *
from application.models.chemicalsModel import *
from application.models.containersModel import *
from application.config import *
from application.logic.getAuthUser import AuthorizedUser


from flask import render_template, \
                          request, \
                          jsonify

@app.route('/migrateChem/', methods = ['GET', 'POST'])
def migrateChem():
    auth = AuthorizedUser()
    user = auth.getUser()
    userLevel = auth.userLevel()
    print user.username, userLevel

    #locdict = Batch.select().dicts().get() This was used for datamodel testing
    if userLevel == 'admin' or userLevel == "systemAdmin":
        if request.method == "GET":
            return render_template("views/MigrateChem.html",
                    config = config)
    

        elif request.method == "POST":
            containerObj = None
            alreadyMoved = False
            #Gets container from new DB by input barcode whether lower or upper case
            try:
                containerObj = Containers.select()\
                        .join(Chemicals, on=(Containers.chemId_id == Chemicals.chemId))\
                        .where((Containers.barcodeId == request.form['barcodeID'])\
                        |(Containers.barcodeId == request.form['barcodeID'].upper()))\
                        .get()
                alreadyMoved = True
            except Exception,e:
                print str(e)
                pass
            if alreadyMoved == False:
                #If not in new DB. Gets the container from old DB by input barcode whether lower or upper case
                try:
                    containerObj = Batch.select()\
                            .join(Main, on =(Batch.NameRaw_id == Main.NameSorted))\
                            .join(Locates, on=(Batch.Id_id == Locates.Location))\
                            .where((Batch.UniqueContainerID == request.form['barcodeID'])|(Batch.UniqueContainerID == request.form['barcodeID'].upper()))\
                            .get() 
                except:
                    pass
            return render_template("views/MigrateChem.html",
                            alreadyMoved = alreadyMoved,
                            container = containerObj, 
                            config = config)
