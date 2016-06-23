from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: Approve and Deny Users
@app.route('/ma/UserAccess/', methods = ['GET', 'POST'])
@require_role('admin')
def UserAccess():
  return render_template("views/ma/UserAccessView.html", config = config)

