from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: Faculty or Staff requesting for a student to have access to the system.
@app.route('/fa/RequestUserAccess/', methods = ['GET'])
@require_role('faculty')
def RequestUserAccess():
  return render_template("views/fa/RequestUserAccessView.html", config = config, userConfig = userConfig)

