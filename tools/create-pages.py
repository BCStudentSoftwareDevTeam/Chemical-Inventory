from configure import Configuration
import argparse
import os, re

parser = argparse.ArgumentParser(description = 'Setup Flask controllers.')

parser.add_argument('--generate', 
                    type = bool, 
                    nargs = '?',
                    default = False,
                    help = 'Generate files as opposed to just testing syntax. True or False.')

args = parser.parse_args()


def checkSyntax (cc):
  if cc.layout:
    for d in cc.layout:
      if 'directory' in d:
        # Check for both a directory name and list of controllers
        if "name" in d["directory"]:
          if ("controllers" in d["directory"]) \
             and (d["directory"]["controllers"] is not None):
            for controller in d["directory"]["controllers"]:
              checkController(controller)  
          else:
            print "Directories must have a non-empty list of controllers."
            exit()
        else:
          print "Directories must have a 'name' tag."
          exit()
      else:
        print "Missing a directory tag."
        exit()
  else:
    print "Missing top-level layout."
    exit()  
  
  return True

def checkController (controller):
  # Controllers need to have a name and a list of handlers.
  if "name" in controller:
    if ("handlers" in controller) and (controller["handlers"] is not None):
      for handler in controller["handlers"]:
        checkHandler(handler)
    else:
      print "Controllers must have a non-empty list of handlers."
      exit()
  else:
    print "Every controller must have a 'name'."
    exit()

def checkHandler(handler):
  # These need to have a 
  # - purpose
  # - route
  # - methods (non-empty list)
  # - function
  # - roles (non-empty list)
  # 
  # Make sure the methods are valid.
  # Make sure the roles are defined in the roles.yaml
  for key in ["purpose", "route", "function", "methods", "roles"]:
    if not key in handler:
      print "Missing a '%s'." % key
      exit()

  if  handler["methods"] is None:
    print "Methods must be a non-empty list."
    exit()
  
  if not methodsAreValid(handler["methods"]):
    print "Invalid method: {0}".format(handler["methods"])
    exit()

  if not rolesAreValid(handler["roles"]):
    print "Invalid role(s): {0}".format(handler["roles"])
    exit()

def methodsAreValid (methods):
  result = False
  valids = ["GET", "POST", "PUT", "DELETE"]
  for m in methods:
    if m in valids:
      result = True
    else:
      print "Role '{0}' is not valid.".format(m)
      exit()
  return result

def rolesAreValid (roles):
  result = False
  definedRoles = Configuration.from_file('config/roles.yaml').configure()
  for r in roles:
    # print "Role: {0}".format(r)
    # print "Defined: {0}".format(definedRoles)
    if r in definedRoles:
      result = True
    else:
      print "Role '{0}' is not defined.".format(r)
      exit()
  return result

if __name__ == "__main__":
  cc = Configuration.from_file('config/controllers.yaml').configure()
  if checkSyntax (cc):
    print "Syntax checks."