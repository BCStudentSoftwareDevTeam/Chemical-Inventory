import glob, os

controllers = []

# print "cwd: {0}".format(os.getcwd())
for file in glob.glob("application/controllers/*Controller.py"):
    # print "File: {0}".format(file)
    controllers.append(os.path.splitext(os.path.basename(file))[0])

print "Found views: {0}".format(controllers)
__all__ = controllers
