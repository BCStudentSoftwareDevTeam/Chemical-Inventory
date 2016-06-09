import glob, os

views = []

print "cwd: {0}".format(os.getcwd())
for file in glob.glob("application/views/*View.py"):
    print "File: {0}".format(file)
    views.append(os.path.splitext(os.path.basename(file))[0])

print "Found views: {0}".format(views)
__all__ = views
