# See the configure documentation for more about
# this library.
# http://configure.readthedocs.io/en/latest/#
from configure import Configuration
from absolutepath import getAbsolutePath

# The configure library provides a pretty interface to our
# configuration data. This module doesn't do anything other
# than
config_path = getAbsolutePath('config/config.yaml')
config = Configuration.from_file(config_path).configure()

# Load the controllers (if needed)
# controllers = Configuration.from_file('controllers.yaml').configure()
# config.controllers = controllers

# Added for splitting up Add New Chemical form config from config
chemConfig_path = getAbsolutePath('config/chemicalConfig.yaml')
chemConfig = Configuration.from_file(chemicalConfig_path).configure()

# Added for add container page
cont_path = getAbsolutePath('config/containerConfig.yaml')
contConfig = Configuration.from_file(contConfig_path).configure()

# Added for check in page
checkInConfig_path = getAbsolutePath('config_path/checkInConfig.yaml')
checkInConfig = Configuration.from_file(checkInConfig_path).configure()

# Added for check out page
checkOutConfig_path = getAbsolutePath('config/OutConfig.yaml')
checkOutConfig = Configuration.from_file(checkOutConfig_path).configure()

#Added for UserAcess page
userConfig_path = getAbsolutePath('config/useraccessConfig.yaml')
userConfig = Configuration.from_file(userConfig_path).configure()

# Added for Manage Location Page
locationConfig_path = getAbsolutePath('config/locationConfig.yaml')
locationConfig = Configuration.from_file(locationConfig_path).configure()

# This adds the application's base directory to the
# configuration object, so that the rest of the application
# can reference it.
import os
config.sys.base_dir = os.path.abspath(os.path.dirname(__file__))
