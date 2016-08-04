from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role
from application.logic.sortPost import *

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: Add Chemical to the database
@app.route('/sa/AddChemical/', methods = ['GET', 'POST'])
@require_role('systemAdmin')
def AddChemical():
  if request.method == "GET":
    return render_template("views/ma/AddChemicalView.html",
                           config = config,
                           chemConfig = chemConfig)
  data = request.form #If there is a form posted to the page
  
  modelData, extraData = sortPost(data, chemicalsModel.Chemicals) #Only get relevant data for the current Model
  chemicalsModel.Chemicals.create(**modelData) #Create instance of Chemical with mapped info in modelData
  return render_template("views/ma/AddChemicalView.html",
                         config = config,
                         chemConfig = chemConfig)
