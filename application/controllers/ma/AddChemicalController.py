from application import app
from application.models import *
from application.models.util import *
from application.config import *
from application.logic.validation import require_role
from application.logic.sortPost import *

from flask import \
    render_template, \
    request, \
    jsonify, \
    url_for

# PURPOSE: Add Chemical to the database
@app.route('/ma/AddChemical/', methods = ['GET', 'POST'])
@require_role('admin')
def maAddChemical():
  if request.method == "GET":
      return render_template("views/ma/AddChemicalView.html",
                             config = config,
                             chemConfig = chemConfig)
  data = request.form #If there is a form posted to the page
  
  modelData, extraData = sortPost(data, chemicalsModel.Chemicals) #Only get relevant data for the current Model
  print modelData
  if modelData['sdsLink'] == None:
    modelData['sdsLink'] = 'https://msdsmanagement.msdsonline.com/af807f3c-b6be-4bd0-873b-f464c8378daa/ebinder/?SearchTerm=%s' %(modelData['name'])
  print modelData['sdsLink']
  chemicalsModel.Chemicals.create(**modelData) #Create instance of Chemical with mapped info in modelData
  return render_template("views/ma/AddChemicalView.html",
                         config = config,
                         chemConfig = chemConfig)
                         
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
    
@app.route('/checkConc/', methods=["GET"])
def checkConc():
  name = request.args.get('chemName')
  conc = request.args.get('concentration')
  try:
    chemical = chemicalsModel.Chemicals.get(chemicalsModel.Chemicals.name == name,
                                            chemicalsModel.Chemicals.concentration == conc)
    return jsonify({status: 'OK'})
  except:
    return jsonify({status: 'Computer says no'})