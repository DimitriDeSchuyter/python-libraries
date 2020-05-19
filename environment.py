#!/usr/bin/env python3

############################################################################
## LIBRARY for MySQL Handling                                             ##
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from echo import echo;
from docker import docker;
from config import config;
from command import command;
import os, sys;

class environment:

    @staticmethod # Environment GET variable
    def get(variable, password = False, prompt = True):
        variable = str(variable);
        if __debug__ :
            echo.debug(variable);
        try:
            value_1 = os.environ[variable];
        except KeyError as e:
            value_1 = None;
        if __debug__ :
            echo.debug(value_1);
        
        try:
            cfg = config("/etc/environment", "SHELL");
            value_2 = cfg.get(None, variable);
        except Exception as e:
            value_2 = None;
        if __debug__ :
            echo.debug(value_2);

        if (value_1 == value_2 and not value_1 == None) or (value_1 == None and not value_2 == None):
            if value_1 == None:
                environment.set(variable, value_2, password);
            return value_2;
        else:
            if prompt:
                value = echo.prompt(variable, password);
                environment.set(variable, value, password);
                return value;
            else:
                echo.error("Differences in environment values for `" + variable + "`");
                sys.exit(1);
                

    @staticmethod # Environment SET variable
    def set(variable, value, password = False):
        variable = str(variable);
        value = str(value);
        if __debug__:
            echo.debug("setting variable `" + variable + "`");
        try:
            os.environ[variable] = value;
            cfg = config("/etc/environment", "SHELL");            
            cfg.set(None, variable, value);
            cfg.write();
            command.exec("echo $" + variable);
            command.exec("export " + variable);
        except KeyError as e:
            echo.error(str(e));
            sys.exit(1);


class environmentError(Exception):
    pass


if __debug__:
    echo.debug("imported `environment.py`");
