from application import app
from config import *
from flask import \
    render_template, \
    url_for

@app.route('/')
def index():
  return render_template("views/helloView.html", config = config)
