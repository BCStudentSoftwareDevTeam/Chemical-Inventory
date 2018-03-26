from application import app
from application.models.wasteContainersModel import *
from application.models.util import *
from application.config import *
from application.logic.getAuthUser import AuthorizedUser

from flask import \
    render_template, \
    redirect, \
    request, \
    jsonify, \
    url_for, \
    flash, \
    abort

# PURPOSE: Add New Chemical to the database
@app.route('/AddWaste/', methods = ['GET', 'POST'])
def AddWaste():
  auth = AuthorizedUser()
  user = auth.getUser()
  userLevel = auth.userLevel()
  print user.username, userLevel

  if userLevel == "admin" or userLevel == "systemAdmin":
    if request.method == "GET":
        return render_template("views/AddWasteView.html",
                               authLevel = userLevel,
                               config = config,
                               chemConfig = chemConfig,
                               wasteConfig = wasteConfig)

    status, flashMessage, flashFormat, wCont = createWaste(request.form) # Function located in chemicalsModel.py
    flash(flashMessage, flashFormat)
    #if status: # Chemical created successfully
    #  return redirect(url_for('ViewChemical', chemId = newChem.chemId)) #Redirect to the new chemical page
    #else:
    return render_template("views/AddWasteView.html",
                             authLevel = userLevel,
                             config = config,
                             chemConfig = chemConfig,
                             wasteConfig = wasteConfig)

  else:
    abort(403)
