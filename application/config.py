import yaml
import os

# Read and parse the config.yaml file
with open('config/config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Read and parse the chemicalConfig.yaml file
with open('config/chemicalConfig.yaml', 'r') as f:
    chemConfig = yaml.safe_load(f)

# Read and parse the containerConfig.yaml file
with open('config/containerConfig.yaml', 'r') as f:
    contConfig = yaml.safe_load(f)

# Read and parse the checkInConfig.yaml file
with open('config/checkInConfig.yaml', 'r') as f:
    checkInConfig = yaml.safe_load(f)

# Read and parse the OutConfig.yaml file
with open('config/OutConfig.yaml', 'r') as f:
    checkOutConfig = yaml.safe_load(f)

# Read and parse the useraccessConfig.yaml file
with open('config/useraccessConfig.yaml', 'r') as f:
    userConfig = yaml.safe_load(f)

# Read and parse the locationConfig.yaml file
with open('config/locationConfig.yaml', 'r') as f:
    locationConfig = yaml.safe_load(f)

# Read and parse the locations.yaml file
with open('config/locations.yaml', 'r') as f:
    addLocationConfig = yaml.safe_load(f)

# Read and parse the reports.yaml file
with open('config/reports.yaml', 'r') as f:
    reportConfig = yaml.safe_load(f)

# Add the application's base directory to the config object
config['sys']['base_dir'] = os.path.abspath(os.path.dirname(__file__))

from application import app
from application.customFilters import filters
app.jinja_env.filters['formatDateTime'] = filters.formatDateTime
