from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: CheckOut a chemical
@app.route('/sa/CheckOut/', methods = ['GET', 'POST'])
@require_role('systemAdmin')
@require_role('masterAdmin')
def CheckOut():
  return render_template("views/sa/CheckOutView.html", config = config)

