#!/usr/bin/env python3

############################################################################
## LIBRARY for MySQL Handling                                             ##
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from . import command, config, echo
import os, sys

DEFAULT_FILENAME = "~/.env"

class Environment:
    def __init__(self, filename = DEFAULT_FILENAME):
        self.setFile(filename)        

    # Environment SET file
    def setFile(self, filename):
        #self.config.close # TODO Close Current file        
        self.filename = str(filename)
        echo.debug('Opening `'+ self.filename +'` as Environment File.')
        self.config = config.Config(self.filename,"SHELL")

    # Environment GET file
    def getFile(self):
        return self.filename

    # Environment REQUIRE file
    def require(self, variable, password = False):
        variable = str(variable)
        try:
            value = str(self.config.require(None, variable))
            self.config.write()
            echo.debug(variable + ': ' + value)
            return value
        except Exception as e:            
            echo.error(str(e))
            raise e

    # Environment GET variable
    def get(self, variable, password = False):
        variable = str(variable)
        try: # Trying to get the variable from system environment
            value = self.config.get(None, variable)            
            echo.debug(variable + ': ' + value)
        except config.NoOptionError as e:
            raise NoOptionError()
        except Exception as e:            
            echo.error(str(e))
            raise e

    # Environment SET variable
    def set(self, variable, value, password = False):
        variable = str(variable)
        value = str(value)
        echo.debug("Setting variable `" + variable + "`")
        try:
            #os.environ[variable] = value
            self.config.set(None, variable, value)
            self.config.write()
            #command.exec("echo $" + variable)
            #command.exec("export " + variable)
        except config.NoOptionError as e:
            raise NoOptionError()
        except KeyError as e:            
            echo.error(str(e))
            raise e

def get(variable, password = False):
    variable = str(variable)
    try: # Trying to get the variable from system environment
        value = str(os.environ[variable])           
        echo.debug(variable + ': ' + value)
        return value
    except Exception as e:            
        echo.error(str(e))
        raise e

class NoOptionError(Exception):
    pass
