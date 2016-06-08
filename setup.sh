# This sets default values for the versions of the Python
# libraries we are installing. If we wish to override this
# (say, during VM or container setup), we do so by
# exporting these variables into the shell environment before
# sourcing this script. If these variables exist before this
# script is sourced, then the pre-existing values will be used.
FLASK_VERSION="${FLASK_VERSION:-0.11.1}"
PEEWEE_VERSION="${PEEWEE_VERSION:-2.8.1}"
PYYAML_VERSION="${PYYAML_VERSION:-3.11}"
CONFIGURE_VERSION="${CONFIGURE_VERSION:-0.5}"

# If there is a virtual environment, destroy it.
if [ -d venv ]; then
  echo "Deactivating and removing old virtualenv"
  deactivate 2>&1 /dev/null
  rm -rf venv 2>&1 /dev/null
fi

# Create and activate a clean virtual environment.
virtualenv venv
. venv/bin/activate

# Create a data directory
# We will want this if it is a new project.
mkdir -p data

# Upgrade pip before continuing; avoids warnings.
# This should not affect application behavior.
pip install --upgrade pip

# Install specific versions of libraries to avoid
# different behaviors of applications over time.

pip install "flask==$FLASK_VERSION"
# http://flask.pocoo.org/
pip install "peewee==$PEEWEE_VERSION"
# http://docs.peewee-orm.com/en/latest/
pip install "configure==$CONFIGURE_VERSION"
# http://configure.readthedocs.io/en/latest/#
