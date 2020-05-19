#!/usr/bin/env python3

############################################################################
## LIBRARY for MySQL Handling                                             ##
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from echo import echo;
from docker import docker;
from environment import environment;
import os, sys;

class mysql:

    @staticmethod # DOCKER CMD
    def query(sql):
        if __debug__:
            echo.debug(sql);
        container = environment.get("DB_CONTAINER_NAME");
        password = environment.get("DB_ROOT_PASSWORD");
        docker.exec("-it",container,"mysql -u root --password=" + password + " -e \"" + sql.replace("\\","\\\\").replace("\"","\\\"") + "\"");        

    class database:
        @staticmethod # DB CREATE
        def create(db_name):
            sql = "CREATE DATABASE " + db_name + ";";
            mysql.query(sql);

    class user:
        @staticmethod # USER CREATE
        def create(username, password, container = "*", network = "db"):
            if container != "*":
                docker.container.exists(container);
            docker.network.exists(network);
            sql = "CREATE USER '" + username+ "'@'" + container + "." + network + "' IDENTIFIED BY '" + password + "';";
            mysql.query(sql);

        @staticmethod # USER GRANT
        def grant(username, database, container = "*", network = "db"):
            if container != "*":
                docker.container.exists(container);
            docker.network.exists(network);
            sql = "GRANT ALL PRIVILEGES ON " + database + ".* TO '" + username + "'@'" + container + "." + network + "';";
            mysql.query(sql);

class mysqlError(Exception):
    pass

if __debug__:
    echo.debug("imported `mysql.py`");
