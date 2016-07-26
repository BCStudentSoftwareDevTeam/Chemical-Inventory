from application import app
from application.models.chemicalsModel import *
from application.models.containersModel import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    json as simplejson, \
    url_for

# PURPOSE: CheckIn a container
@app.route('/ma/CheckIn/', methods = ['GET', 'POST'])
@require_role('admin')
def maCheckIn():

  if request.method == "GET":
    return render_template("views/ma/CheckInView.html",
                           config = config,
                           contConfig = contConfig,
                           checkInConfig = checkInConfig,
                           container = None)
  
@app.route('/checkInData/', methods = ['GET'])
def checkInData():
    barId = request.args.get('barId')
    container = Containers.select().where(Containers.barcodeId == barId).dicts().get()
    # chemical = Chemicals.select().join(Containers).where(Containers.barcodeId == barId).dicts().get()
    return render_template("snips/setVars.html",
                           avatar_url = process_data(data),
                           container = container)