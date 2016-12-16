from application import app
from application.models.chemicalsModel import *
from application.models.util import *
from application.config import *
from application.logic.getAuthUser import AuthorizedUser

from flask import \
    render_template, \
    request, \
    jsonify, \
    url_for, \
    abort

# PURPOSE: Add New Chemical to the database
@app.route('/AddChemical/', methods = ['GET', 'POST'])
def AddChemical():
  auth = AuthorizedUser()
  user = auth.getUser()
  userLevel = auth.userLevel()
  print user.username, userLevel
  
  if userLevel == "admin" or userLevel == "systemAdmin":  
    if request.method == "GET":
        return render_template("views/AddChemicalView.html",
                               config = config,
                               chemConfig = chemConfig)
    
    createChemical(request.form) # Function located in chemicalsModel.py
    
    return render_template("views/AddChemicalView.html",
                           config = config,
                           chemConfig = chemConfig,
                           authLevel = userLevel)
  else:
    abort(403)
 
@app.route('/checkName/', methods=['GET'])
def checkName():
  nameVal = request.args.get('value')
  try:
    chemical = chemicalsModel.Chemicals.get(chemicalsModel.Chemicals.name == nameVal)
    if chemical is not None:
      return jsonify({'required':True}) #Build the json dict for a success
  except:
    print "This should log something..."
    return jsonify({'required':False})