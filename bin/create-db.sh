#!/bin/sh

# Create Application Database and User
# ---
# This script will use the `psql` command to run SQL commands that
# will create the needed database and user for this application.
# A running PostgreSQL server is necessary.
#
# NOTE: You only need to run this script once.
#
# Run with the following command in the project's root directory:
# $ sh bin/create-db.sh

# create user for the application
psql postgres -c 'CREATE USER schedule_user;'

# create development database and grant access to application user
psql postgres -c 'CREATE DATABASE schedule;'
psql postgres -c 'GRANT ALL PRIVILEGES ON DATABASE "schedule" to schedule_user;'

# create test database and grant access to application user
psql postgres -c 'CREATE DATABASE schedule_test;'
psql postgres -c 'GRANT ALL PRIVILEGES ON DATABASE "schedule_test" to schedule_user;'

