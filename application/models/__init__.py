import glob, importlib, os, re

models = []

# print "cwd: {0}".format(os.getcwd())
directoryOfThisFile = os.path.dirname(os.path.realpath(__file__))
for file in glob.glob(directoryOfThisFile + "/*Model.py"):
    # print "File: {0}".format(file)
    models.append(os.path.splitext(os.path.basename(file))[0])

# print "Found models: {0}".format(models)

def classFromName(moduleName, className):
    # load the module, will raise ImportError if module cannot be loaded
    m = importlib.import_module(moduleName)
    # get the class, will raise AttributeError if class cannot be found
    c = getattr(m, className)
    return c

def getModelClasses():
  classes = []
  for m in models:  
    moduleName = "application.models.{0}".format(m) 
    className  = re.sub("Model", "", m).capitalize()
    # print "Module Name: {0}\nClass Name: {1}".format(moduleName, className)
    c = classFromName(moduleName, className)
    classes.append(c)
  return classes

def getModelFromName (name):
  c = None
  for m in models:  
    moduleName = "application.models.{0}".format(m) 
    className  = re.sub("Model", "", m).capitalize()
    if className == name:
      c = classFromName(moduleName, className)
  return c
    

classes = getModelClasses()