from application import app
from application.config import *
from functools import wraps
from flask import \
    render_template, \
    url_for
    
# https://realpython.com/blog/python/primer-on-python-decorators/
def checkValidUser (fun):
  @wraps(fun)
  def wrapper (*args, **kwargs):
    print "Is Valid User"
    return fun(*args, **kwargs)
  return wrapper

def checkValidRole (*expected_args):
  def decorator (fun):
    @wraps(fun)
    def wrapper (*args, **kwargs):
      print "Is Valid Role: %s" % expected_args[0]
      return fun(*args, **kwargs)
    return wrapper
  return decorator

def accept_any_role(*args):
  return checkValidRole(args)
  
@app.route("/scott/<int:age>")
@accept_any_role("programChair", "divisionChair", "admin")
def scottControllerHandler (age):
  print "Handler Called"
  return str(age)
