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
                ########
                INIT = -1    #Inial start state(Not really needed but looks nice)
                MIGRATED = 0 #Both Chemical and Container already Migrated
                ONLYCHEM = 1 #Only Chemical has been Migrated. Container needs to be migrated
                NIETHER = 2  #Both Chemical and Container need to be migrated
                UNKNOWN = 3  #This container does not exist anywhere
                ########
                inputBar = request.form['barcodeID']
                state = INIT
                containerObj = None
                chemObj = None
                ########
                #Gets container from new DB by input barcode whether lower or upper case
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

                ########
                #If not already Migrated checks if chemical is migrated
                if state != MIGRATED:
                    #Try and Retrieve Container and Chemical Informatoin from CISPro
                    try:
                        containerObj = Batch.select()\
                                .join(Main, on =(Batch.NameRaw_id == Main.NameSorted))\
                                .join(Locates, on=(Batch.Id_id == Locates.Location))\
                                .where((Batch.UniqueContainerID == inputBar)|(Batch.UniqueContainerID == inputBar.upper())).get()
                    except:
                        #Not in CISPro
                        state = UNKNOWN
                
                    ########
                    #If Continer in CISPro check if parent Chemical is Migrated
                    if state != UNKNOWN: #If the container is found in the old system. Check for Chem
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
				    authLevel = userLevel)
                        except Exception, e:
                            #Chemical is not yet in BCCIS
                            print str(e)
                            state = NIETHER
                            return render_template("views/MigrateChem.html",
                                    state = state,
                                    container = containerObj,
                                    chemInfo = chemObj,
                                    inputBar = inputBar,
                                    config = config,
                                    chemConfig = chemConfig,
				    authLevel = userLevel)
                            ##########
                            ###
                            ###YOU ARE STUCK HERE FROM NOT RECOGNIZING THIS FILE PATH
                            ###THIS IS WHEN YOU INPUT N1-15
                            ###
                            ##########
                    else:
                        pass

                return render_template("views/MigrateChem.html",
                                state = state,
                                container = containerObj,
                                chemical = chemObj,
                                inputBar = inputBar,
                                config = config,
                                contConfig = contConfig,
				authLevel = userLevel)
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
                    flash("Container could not be added")
                return render_template("views/MigrateChem.html",
                        config = config)

            elif request.form['formName'] == 'addChem':
                for i in data: #Loop through the keys in the form dictionary
                    setattr(chemInfo, i, data[i]) #Set the attribute, 'i' (the current key in the form), of 'chemInfo' (the chemical) to the value of the current key in the form
                chemInfo.save()
                return render_template('views/MigrateChem.html',
                        config = config)
            #Left Off here
            #elif request.form[] == 'addCont':
                ##BUILD OUT WITH ZACHS CODE FROM THE MERGE. ViewContainer.html
