# See the configure documentation for more about
# this library.
# http://configure.readthedocs.io/en/latest/#
from configure import Configuration
from config import config
from application.models import getModelFromName
import re

roleConfig = Configuration.from_file('roles.yaml').configure()

def userHasRole (username, role):
  # print "Checking role: {0}".format(role)
  
  for ug in roleConfig[role]:
    # We may be referencing another "group," which is a role.
    # Recursively search.

    # If the ug is an exact match for the username, it means we 
    # have directly coded a username into a group. We should 
    # return True, because we want them to have access. 
    if ug == config.flask.username:
      return True
    
    if re.match('group', ug):
      superRole = re.split(" ", ug)[1]
      return userHasRole (username, superRole)
      
    # We may find it is a database lookup.
    if re.match('database', ug):
      # Get the name of the database
      db = re.split(" ", ug)[1]
      # Get the actual model from the name of the model.
      m = getModelFromName(db)
      #print "Model: {0}".format(m)
      
      # Do a "get", and require that their username and role are both
      # set. For example, look for {jadudm, admin}, not just the username.
      result = m.select().where(m.username == username, m.role == role).count()
      #print "User '{0}' validated via database {1}".format(username, db) 
      return result > 0
    
    # Check if they are in the Active Directory
    if re.match('AD', ug):
      # FIXME: Implement this.
      return False
      
    # If the keyword "ANY" appears, it means anyone 
    # is good to go.
    if re.match("ANY", ug):
      return True
      
    else:
      return False  
  
def getRoles(username):
  roles = []
  for role in roleConfig:
    if userHasRole (username, role):
      roles.append(role)
  return roles
