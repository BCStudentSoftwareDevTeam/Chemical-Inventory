if [ -d venv ]; then
  echo "Deactivating and removing old virtualenv"
  deactivate 2>&1 /dev/null
  rm -rf venv
fi

virtualenv venv
. venv/bin/activate

pip install --upgrade pip

pip install flask
pip install peewee
pip install flask-wtf
pip install pyyaml
pip install configure

# Install known good SQLite
rm -rf .tmp
mkdir .tmp
pushd .tmp
  git clone https://github.com/rogerbinns/apsw
  pushd apsw
    # Fetch the source for SQLite
    python setup.py fetch --all 
    # Build the SQLite source with known extensions/parameters
    python setup.py build --enable-all-extensions
    # Install the Python module into our virtualenv
    python setup.py install
    # We won't always test.
    # python setup.py test
  popd
popd
