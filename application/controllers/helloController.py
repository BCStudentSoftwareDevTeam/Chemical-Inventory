from application import app
from application.config import *
from flask import \
    render_template, \
    url_for

@app.route("/", methods = ["GET"])
def index():
  return render_template ("views/stu/helloView.html", config = config)



