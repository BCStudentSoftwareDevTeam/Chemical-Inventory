import glob, os

models = []

# print "cwd: {0}".format(os.getcwd())
directoryOfThisFile = os.path.dirname(os.path.realpath(__file__))
for file in glob.glob(directoryOfThisFile + "/*Model.py"):
    # print "File: {0}".format(file)
    models.append(os.path.splitext(os.path.basename(file))[0])

# print "Found models: {0}".format(models)
__all__ = models
