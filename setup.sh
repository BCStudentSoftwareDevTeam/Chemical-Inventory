#!/usr/bin/env bash

# Check for correct python version
VERSION=`python3 --version | awk '{print $2}'`
if [ "${VERSION:0:1}" -ne "3" ] || [ "${VERSION:2:1}" -lt "7" ] || [ "${VERSION:2:1}" -gt "9" ]; then
    echo "You must use Python > 3.7. You are using $VERSION"
    echo "When upgrading, remember to install python3.X-dev and python3.X-venv (and maybe the right pip)"
    #return 1
else
    echo -e "You are using Python $VERSION"
fi

# Create a virtual environment for dependencies
if [ ! -d venv ]
then
  python3 -m venv venv
fi
. venv/bin/activate

# Create a data directory, in case it does not exist
mkdir -p data

# Upgrade pip before continuing
python3 -m pip install --upgrade pip

# install requirements
python3 -m pip install -r requirements.txt

# XXX Re-do config file to be like newer apps?
# XXX mention database setup

export FLASK_APP=run.py
export FLASK_ENV=development
export FLASK_RUN_PORT=8080
export FLASK_RUN_HOST=0.0.0.0   # To allow external routing to the application for development
