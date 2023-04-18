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

if [ ! -d venv ]
then
  python3 -m venv venv
fi
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
