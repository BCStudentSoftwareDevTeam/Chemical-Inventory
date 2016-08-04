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
@app.route('/sa/CheckIn/', methods = ['GET', 'POST'])
@require_role('admin')
def saCheckIn():

  if request.method == "GET":
    return render_template("views/sa/CheckInView.html",
                           config = config,
                           contConfig = contConfig,
                           checkInConfig = checkInConfig,
                           container = None) #container = None is needed as a placeholder for the page before the barcode is entered.