from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: Home page and dash boeard for EHS staff/system admins.
@app.route('/sa/SystemAdminHome/', methods = ['GET'])
@require_role('systemAdmin')
def SystemAdminHome():
  return render_template("views/sa/SystemAdminHomeView.html", config = config)

