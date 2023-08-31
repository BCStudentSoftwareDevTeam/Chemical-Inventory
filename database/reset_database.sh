#!/bin/bash

PRODUCTION=0
if [ "`hostname`" == 'CS-CHEMICAL' ]; then
	echo "DO NOT RUN THIS SCRIPT ON PRODUCTION UNLESS YOU REALLY REALLY KNOW WHAT YOU ARE DOING"
	PRODUCTION=1
	exit 1;
fi

cd database/

########### Process Arguments ############
BACKUP=0
BASE=0
TEST=1
if [ "$1" == "from-backup" ]; then
	BACKUP=1
	TEST=0
elif [ "$1" == "base" ]; then
	BASE=1
	TEST=0
elif [ "$1" == "test" ]; then
	:
else
    echo "You must specify which data set you want to restore"
    echo "Usage: ./reset_database.sh [from-backup|base|test]"
    exit;
fi



########### Recreate Database Schema ###########
echo "Dropping databases"
mysql -u root -proot --execute="DROP DATABASE \`chemical\`; DROP USER 'chemical_user';"

echo "Recreating databases and users"
mysql -u root -proot --execute="CREATE DATABASE IF NOT EXISTS \`chemical\`; CREATE USER IF NOT EXISTS 'chemical_user'@'%' IDENTIFIED BY 'password'; GRANT ALL PRIVILEGES ON *.* TO 'chemical_user'@'%';"


# remove ahead of time in case we didn't clean up last time
rm -rf migrations
rm -rf migrations.json

echo -n "Creating database objects"
if [ $BACKUP -eq 1 ]; then
    echo " from backup"
    mysql -u root -proot chemical < prod-backup.sql
else
    echo " empty"
    ./migrate_db.sh
fi

# remove so we do a fresh migration next time
if [ $PRODUCTION -ne 1 ]; then
    rm -rf migrations
    rm -rf migrations.json
fi


############ Add Data (if needed) ##############

# Adding data we need in all environments, unless we are restoring from backup
if [ $BACKUP -ne 1 ]; then
    python3 base_data.py
else
    echo "You have imported the production DB backup."
fi

# Adding fake data for non-prod, set up admins for prod
if [ $PRODUCTION -eq 1 ]; then
    echo "Nothing to do right now"

elif [ $BACKUP -ne 1 ]; then
    if [ $TEST -eq 1 ]; then
	    python3 test_data.py
    fi
fi

# NOW we can re-run our tests
touch ../setup.sh