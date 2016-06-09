from application import app
from application.models import *
from config import *

from flask import request


@app.route ('/insert', methods = ["POST"])
def insert ():
  data = request.form['data']
  id   = request.form['id']
  size = len(data)
  new_mess = Mess(id = id, data = data, size = size)
  new_mess.save()
  return "OK"
