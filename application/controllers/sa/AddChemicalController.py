from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: Add Chemical to the database
@app.route('/sa/AddChemical/', methods = ['GET', 'POST'])
@require_role('systemAdmin')
@require_role('admin')
def AddChemical():
  if request.method == "GET":
      return render_template("views/sa/AddChemicalView.html", config = config, chemConfig = chemConfig)
  data = request.form
  
  modelData, extraData = sortPost(data, chemicalsModel.Chemicals)
  chemicalsModel.Chemicals.create(**modelData)
  return render_template("views/sa/AddChemicalView.html", config = config, chemConfig = chemConfig)

