#!/usr/bin/env python3

############################################################################
## LIBRARY for MySQL Handling                                             ##
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from . import command, config, echo
import os, sys

DEFAULT_PATH = "~/.env"

def get(variable, default = None):
    try:
        return os.environ[variable]
    except KeyError as e:
        if not default == None: return default 
        else: raise e


class Environment(config.Shellconfig):
    
    def __init__(self, path = DEFAULT_PATH):
        return super().__init__(path)

    # Environment REQUIRE
    def require(self, variable, default = None):
        try: default = get(variable, default)
        except KeyError as e: default = None
        return super().require(variable, default)

    # Environment GET
    def get(self, variable, default = None):
        try: default = get(variable, default)
        except KeyError as e: default = None
        return super().get(variable, default)

    # Environment SET
    def set(self, variable, value):
        command.exec("export " + variable + "=" + value)
        return super().set(variable, value)
