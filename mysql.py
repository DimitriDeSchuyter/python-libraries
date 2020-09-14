#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from . import echo, docker, environment
import os, sys

def query(sql):
    if __debug__:
        echo.debug(sql)
    container = environment.get("DB_CONTAINER_NAME")
    password = environment.get("DB_ROOT_PASSWORD")
    docker.exec("-it",container,"mysql -u root --password=" + password + " -e \"" + sql.replace("\\","\\\\").replace("\"","\\\"") + "\"")

class Database:
    @staticmethod # DB CREATE
    def create(db_name):
        sql = "CREATE DATABASE " + db_name + ";"
        query(sql)

class User:
    @staticmethod # USER CREATE
    def create(username, password, container = "*", network = "db"):
        if container != "*":
            docker.Container.exists(container)
        docker.Network.exists(network)
        sql = "CREATE USER '" + username+ "'@'" + container + "." + network + "' IDENTIFIED BY '" + password + "';"
        query(sql)

    @staticmethod # USER GRANT
    def grant(username, database, container = "*", network = "db"):
        if container != "*":
            docker.Container.exists(container)
        docker.Network.exists(network)
        sql = "GRANT ALL PRIVILEGES ON " + database + ".* TO '" + username + "'@'" + container + "." + network + "';"
        query(sql)

class MysqlError(Exception):
    pass