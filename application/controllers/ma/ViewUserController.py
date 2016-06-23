from application import app
from application.models import *
from application.config import *
from application.logic.validation import require_role

from flask import \
    render_template, \
    request, \
    url_for

# PURPOSE: View all the user and add new users 
@app.route('/ma/ViewUser/', methods = ['GET', 'POST'])
@require_role('admin')
def ViewUser():
  return render_template("views/ma/ViewUserView.html", config = config)

