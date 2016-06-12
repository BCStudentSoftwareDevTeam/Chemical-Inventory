
import glob, os

controllers = []

directoryOfThisFile = os.path.dirname(os.path.realpath(__file__))
# print "cwd: {0} thisFile: {1}".format(os.getcwd(), directoryOfThisFile)

for file in glob.glob(directoryOfThisFile + "/*Controller.py"):
    # print "File: {0}".format(file)
    controllers.append(os.path.splitext(os.path.basename(file))[0])

for subdir in glob.glob(directoryOfThisFile):
  if os.path.isdir(subdir):
    controllers.append(os.path.splitext(subdir + "/" + os.path.basename(file))[0])
      
print "Found controllers: {0}".format(controllers)
__all__ = controllers

#import pkgutil

#__all__ = []
#for loader, module_name, is_pkg in  pkgutil.walk_packages(__path__):
#    __all__.append(module_name)
 #   module = loader.find_module(module_name).load_module(module_name)
#    exec('%s = module' % module_name)