from application import app
from application.models import *
from application.models.util import *
from application.config import *
from application.logic.getAuthUser import AuthorizedUser
from application.logic.sortPost import *

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
        return render_template("views/ma/AddChemicalView.html",
                               config = config,
                               chemConfig = chemConfig)
    data = request.form #If there is a form posted to the page
    
    modelData, extraData = sortPost(data, chemicalsModel.Chemicals) #Only get relevant data for the current Model
    if modelData['sdsLink'] == None:
      modelData['sdsLink'] = 'https://msdsmanagement.msdsonline.com/af807f3c-b6be-4bd0-873b-f464c8378daa/ebinder/?SearchTerm=%s' %(modelData['name'])
    print modelData['sdsLink']
    chemicalsModel.Chemicals.create(**modelData) #Create instance of Chemical with mapped info in modelData
    return render_template("views/ma/AddChemicalView.html",
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