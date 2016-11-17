from application import app
from application.models.staticModels.batchModel import *
from application.models.staticModels.mainModel import *
from application.models.staticModels.locatesModel import *
from application.models.chemicalsModel import *
from application.models.containersModel import *
from application.models.roomsModel import *
from application.models.storagesModel import *
from application.models.buildingsModel import *
from application.models.historiesModel import *
from application.config import *
from application.logic.getAuthUser import AuthorizedUser
from application.logic.sortPost import *


from flask import render_template, \
                          request, \
                          jsonify, \
                          redirect, \
                          flash

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
		    authLevel = userLevel,
                    config = config
                    )

        elif request.method == "POST":
            data = request.form
            if request.form['formName'] == "searchBcode":
               return renderCorrectTemplate(request.form['barcodeID'])
            elif request.form['formName'] == 'addCont':
                ###
                ##Process the form of adding a Container
                ###
                try:
                    modelData, extraData = sortPost(data, Containers)
                    cont = Containers.create(**modelData)
                    Histories.create(movedTo = modelData['storageId'],
                                    containerId = cont.conId,
                                    modUser = extraData['user'],
                                    action = "Created",
                                    pastQuantity = "%s %s" %(modelData['currentQuantity'], modelData['currentQuantityUnit']))
                    flash("Container Successfully Migrated Into System")
                except Exception as e:
                    print str(e)
                    flash("Container Could Not Be Added")
                return render_template("views/MigrateChem.html",
                        config = config,
			authLevel = userLevel)

            elif request.form['formName'] == 'addChem':
                try:
                    data = request.form
                    modelData, extraData = sortPost(data, Chemicals)
                    if modelData['sdsLink'] == None:
                        modelData['sdsLink'] = "https://msdsmanagement.msdsonline.com/af807f3c-b6be-4bd0-873b-f464c8378daa/ebinder/?SearchTerm=%s" %(modelData['name'])
                    Chemicals.create(**modelData)
                    flash("Chemical Was Successfully Added To The DB")
                    print data['barcode']
                    return renderCorrectTemplate(data['barcode'])
                except Exception as e:
                    flash("Chemical Could Not Be Added")

            return render_template('views/MigrateChem.html',
                    config = config,
                    authLevel = userLevel)

def renderCorrectTemplate(barcode):
                auth = AuthorizedUser()
                user = auth.getUser()
                userLevel = auth.userLevel()
                ########
                INIT = -1    #Inial start state(Not really needed but looks nice)
                MIGRATED = 0 #Both Chemical and Container already Migrated
                ONLYCHEM = 1 #Only Chemical has been Migrated. Container needs to be migrated
                NIETHER = 2  #Both Chemical and Container need to be migrated
                UNKNOWN = 3  #This container does not exist anywhere
                ########
                inputBar = barcode.upper()
                state = INIT
                containerObj = None
                chemObj = None
                ########
                try:
                    containerObj = Containers.select()\
                            .join(Chemicals, on=(Containers.chemId_id == Chemicals.chemId))\
                            .where((Containers.barcodeId == inputBar)\
                            |(Containers.barcodeId == inputBar.upper()))\
                            .get()
                    flash("Container " + inputBar + " Already Migrated Into System")
                    state = MIGRATED
                except Exception,e:
                    #print str(e)
                    pass
                #Try and Retrieve Container and Chemical Informatoin from CISPro
                if state != MIGRATED:
                    try:
                        containerObj = Batch.select()\
                            .join(Main, on =(Batch.NameRaw_id == Main.NameSorted))\
                            .join(Locates, on=(Batch.Id_id == Locates.Location))\
                            .where((Batch.UniqueContainerID == inputBar)|(Batch.UniqueContainerID == inputBar.upper())).get()
                    except:
                        #Not in CISPro
                        flash("Container " + inputBar + " Is Not In CISPro Database")
                        state = UNKNOWN
                    if state != UNKNOWN:
                        ########
                        #If Continer in CISPro check if parent Chemical is Migrated
                        try:
                            #Check if parent Chemical is in BCCIS
                            chemObj = Chemicals.select()\
                                .where(Chemicals.oldPK == containerObj.NameRaw_id).get()

                            storageList = Storages.select().order_by(Storages.roomId)

                            buildingList = Buildings.select()

                            state = ONLYCHEM
                            return render_template("views/MigrateChem.html",
                                state = state,
                                container = containerObj,
                                chemInfo = chemObj,
                                inputBar = inputBar,
                                config = config,
                                contConfig = contConfig,
                                storageList = storageList,
                                buildingList = buildingList,
                                barcode = inputBar,
                                authLevel = userLevel,
                                migrated = 1)
                        except Exception, e:
                            #Chemical is not yet in BCCIS
                            #print str(e)
                            state = NIETHER
                            print containerObj.NameRaw.Description
                            return render_template("views/MigrateChem.html",
                                state = state,
                                container = containerObj,
                                chemInfo = chemObj,
                                inputBar = inputBar,
                                config = config,
                                chemConfig = chemConfig,
                                authLevel = userLevel)

                return render_template("views/MigrateChem.html",
                    state = state,
                    container = containerObj,
                    chemical = chemObj,
                    inputBar = inputBar,
                    config = config,
                    contConfig = contConfig,
                    authLevel = userLevel)
