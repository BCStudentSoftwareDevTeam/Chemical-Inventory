# Check for virtualenv
command -v virtualenv >/dev/null 2>&1 || {
  echo >&2 "I require 'virtualenv' but it's not installed.  Aborting.";
  exit 1;
 }

 # Check for pip
command -v pip >/dev/null 2>&1 || {
 echo >&2 "I require 'pip' but it's not installed.  Aborting.";
 exit 1;
}


# If there is a virtual environment, destroy it.
if [ -d venv ]; then
  echo "Deactivating and removing old virtualenv"
  deactivate 2>&1 /dev/null
  rm -rf venv
fi

# Check for correct python version
VERSION=`python3 -V | awk '{print $2}'`
MAJOR_VERSION=`echo $VERSION | cut -d'.' -f1`  #make sure a python version above 3.7 is used 
MINOR_VERSION=`echo $VERSION | cut -d'.' -f2`
if [ $MAJOR_VERSION -eq 3 ] && [ $MINOR_VERSION -ge 7 ]; then
    echo -e "You are using Python $VERSION"
else
    echo "You must use Python 3.7 or later. You are using $VERSION"
    return 1
fi

# Create and activate a clean virtual environment.
virtualenv --python=python3.9 venv
. venv/bin/activate

# Create a data directory
# We will want this if it is a new project.
mkdir -p data

# Upgrade pip before continuing; avoids warnings.
# This should not affect application behavior.
pip3 install --upgrade pip

python -m pip install -r requirements.txt


export FLASK_APP=run.py
export FLASK_ENV=development
export FLASK_RUN_PORT=8080
export FLASK_RUN_HOST=0.0.0.0   # To allow external routing to the application for development
