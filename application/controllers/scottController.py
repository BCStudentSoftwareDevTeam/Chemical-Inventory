from application import app
from config import *
from flask import \
    render_template, \
    url_for

@app.route("/CHANGEME")
def CHANGEME():
  return "CHANGEME"
