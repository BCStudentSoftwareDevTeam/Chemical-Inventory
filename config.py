from configure import Configuration

config = Configuration.from_file('config.yaml').configure()

# Define the application directory
import os
config.sys.base_dir = os.path.abspath(os.path.dirname(__file__))  


