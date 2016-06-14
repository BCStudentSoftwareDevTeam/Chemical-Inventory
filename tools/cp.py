from configure import Configuration
import argparse, os, re, shutil

parser = argparse.ArgumentParser(description = 'Setup Flask controllers.')

parser.add_argument('-g', '--generate', 
                    action = "store_true",
                    help = 'Generate files as opposed to just testing syntax. True or False.')
                    
parser.add_argument('-c', '--config',
                    type = str,
                    help = "Name of the config file to process."
                    )

parser.add_argument('-v', '--verbose', 
                    action = "store_true",
                    help = 'Talk a lot.')

args = parser.parse_args()

def error (msg):
  print "OOPS: {0}\n".format(msg)
  exit()

def announce (msg):
  print msg

def hasLayout (cc):
  return ("layout" in cc)

# http://stackoverflow.com/questions/1835018/python-check-if-an-object-is-a-list-or-tuple-but-not-string
def is_sequence(arg):
    return (not hasattr(arg, "strip") and
            hasattr(arg, "__getitem__") or
            hasattr(arg, "__iter__"))

def isDirectoryDictionary (obj):
  return isinstance(obj, dict) and ("directory" in obj)
          
# http://stackoverflow.com/questions/35784074/does-python-have-andmap-ormap            
def isListOfDirectories (layout):
  return  is_sequence(layout) and \
          all(isDirectoryDictionary(obj) for obj in layout)

def check (d):
  #True if hasLayout (cc) else \
  #  error("Top-level should be a 'layout'.")
  #announce("Layout found.") if args.verbose else False
  True if d["fun"]() else error(d["err"]())
  announce(d["aok"]()) if args.verbose else False
 
def directoriesHaveNames (dirs):
  return all(map(lambda d: "name" in d, dirs))

def nonEmptyControllerList (controllers):
  return is_sequence(controllers) and \
    (len(controllers) > 0)

def controllersAreDictionaries (controllers):
  return all(isinstance(obj, dict) for obj in controllers)

def controllerHasName (c):
  return isinstance(c, dict) and ("name" in c)

def hasHandlerKey (c):
  return "handlers" in c
  
def controllerHasListOfHandlers (handlers):
  return is_sequence(handlers) and \
    len(handlers) > 0

def checkForRoute (h):
  return isinstance(h, dict) and ("route" in h)

def checkHandlerHasKey (h, key):
  return key in h

def checkValidMethods (h):
  result = True
  for m in h["methods"]:
    if not m in ["GET", "POST", "PUT", "DELETE"]:
      print "==> {0} is not a valid method.".format(m)
      result = False
  return result 

def checkValidRoles (h):
  result = True
  definedRoles = Configuration.from_file('config/roles.yaml').configure()
  for r in h["roles"]:
    if not r in definedRoles:
      print "==> {0} is not a valid role.".format(r)
      result = False
  return result


"""
    check ({'fun': lambda: ,
      'err': lambda: "",
      'aok': lambda: ""
    })
"""
def checkSyntax (cc):
  
  check ({'fun': lambda: hasLayout(cc), 
    'err': lambda: "Top-level should be a 'layout'.",
    'aok': lambda: "Layout found."
  })

  directories = cc["layout"]
  check ({'fun': lambda: isListOfDirectories (directories),
    'err': lambda: "The file should begin as a list of 'directory' dictionaries.",
    'aok': lambda: "Layout contains a list of 'directory' dictionaries."
  })
  
  check ({'fun': lambda: directoriesHaveNames (directories),
    'err': lambda: "Every directory should have a 'name' key.",
    'aok': lambda: "All directories have a name."
  })
  
  # We now know there is a valid list of controllers in every directory
  for d in directories:
    print "------------------"
    print "Checking directory '{0}'".format(d["name"])
    print "------------------"
    
    controllers = d["controllers"]
    
    check ({'fun': lambda: nonEmptyControllerList (controllers),
      'err': lambda: "Directory '{0}' has a non-empty list of controllers.".format(d["name"]),
      'aok': lambda: "Directory '{0}' has a list of controllers.".format(d["name"])
    })

    check ({'fun': lambda: controllersAreDictionaries (controllers),
      'err': lambda: "Directory '{0}' has a non-dictionaries in its list of controllers.".format(d["name"]),
      'aok': lambda: "Directory '{0}' has a list of controller dicts.".format(d["name"])
    })
    
    # Now, we check every controller
    for c in controllers:
      check ({'fun': lambda: controllerHasName(c),
        'err': lambda: "Directory '{0}' has a controller missing a 'name'.".format(d["name"]),
        'aok': lambda: "Controller '{0}' has a name.".format(c["name"])
      })
      
      check ({'fun': lambda: hasHandlerKey(c),
        'err': lambda: "'{0}' is missing a 'handlers' key.".format(c["name"]),
        'aok': lambda: "'{0}' has a 'handlers' key.".format(c["name"])
      })
      
      # We know we have the key now.
      handlers = c["handlers"]
      check ({'fun': lambda: controllerHasListOfHandlers(handlers),
        'err': lambda: "Controller '{0}' does not have a list of handlers.".format(c["name"]),
        'aok': lambda: "Controller '{0}' has a list of handlers.".format(c["name"])
      })
      
      # Check each handler
      for h in handlers:
        check ({'fun': lambda: checkForRoute(h),
          'err': lambda: "'{0}' has a handler missing a route.".format(c["name"]),
          'aok': lambda: "Route for '{0}' in '{1}' has a route".format(h["route"], c["name"])
        })

        # Are they all a complete handler
        for key in ["purpose", "route", "methods", "function", "roles"]:
          check ({'fun': lambda: checkHandlerHasKey (h, key),
            'err': lambda: "Handler for route '{0}' is missing '{1}'.".format(h["route"], key),
            'aok': lambda: "Handler for route '{0} has key '{1}'.".format(h["route"], key)
          })
        
        # Make sure we only have valid methods.
        check ({'fun': lambda: checkValidMethods (h),
          'err': lambda: "Handler for route '{0}' has invalid methods.".format(h["route"]),
          'aok': lambda: "Handler for '{0}' has valid methods.".format(h["route"])
        })

        check ({'fun': lambda: checkValidRoles (h),
          'err': lambda: "Handler for route '{0}' has invalid roles.".format(h["route"]),
          'aok': lambda: "Handler for '{0}' has valid roles.".format(h["route"])
        })
        
        check ({'fun': lambda: 1,
          'err': lambda: "",
          'aok': lambda: ""
        })
        
        
    

if __name__ == "__main__":
  if args.config is None:
    cc = Configuration.from_file('config/controllers.yaml').configure()
  else:
    cc = Configuration.from_file(args.config).configure()
  
  syntaxOK = checkSyntax (cc)
  
  if syntaxOK:
    print "Syntax checks."
  
  if syntaxOK and args.generate:
    generateFiles (cc)