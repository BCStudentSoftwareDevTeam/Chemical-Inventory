from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: Add Container for a certain chemical
@app.route('/sa/AddContainer/', methods = ['GET', 'POST'])
@require_role('systemAdmin')
def saAddContainer():
  return render_template("views/sa/saAddContainerView.html", config = config)

