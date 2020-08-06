#!/usr/bin/env python3

############################################################################
## LIBRARY for File Handling                                              ##
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

import configparser
from . import echo, environment, file
import pprint

class Config:
    def __init__(self, filename, configtype = "INI"):
        self.filename = str(filename) #TODO: Check if file exists        
        self.type = configtype
        self.parser = None
        self.read()

    def read(self):
        self.parser = configparser.ConfigParser()
        file.CREATE_IF_NOT_EXISTS = True
        self.handle = file.File(self.filename, 'r')        
        if self.type == "SHELL":
            self.parser.read_string('[DEFAULT]\n' + self.handle.read())            
        elif self.type == "INI":
            self.parser.read(self.handle)
        else:
            raise Exception("Config type unsupported")    
        self.handle.close()

    def require(self, section, variable):
        try:            
            # Check whether the variable is already declared in the file
            return self.get(section, variable)
        except (self.NoOptionError) as e:
            try:
                # Check whether the variable is available in the system environment
                value = self.set(section, variable, environment.get(variable))
                echo.notice("Using system environment variable for " + variable)
                return value
            except environment.NoOptionError as e:
                try:
                    # Prompt the user for the variable and write it direcly in the file
                    value = self.set(section, variable, echo.prompt(variable))
                except Exception as e:                    
                    echo.error(str(e))
                    raise e

    def set(self, section, variable, value):
        try:            
            self.parser.set(section, variable, value)
        except (configparser.NoSectionError) as e:
            self.parser.add_section(section)
            self.parser.set(section, variable, value)  
        except Exception as e:            
            echo.error(str(e))
            raise e

    def get(self, section, variable):
        if section == None:
            try:
                return self.parser.get("DEFAULT", variable).strip("\"")
            except (configparser.NoSectionError, configparser.NoOptionError) as e:
                for section in self.parser.sections():
                    try:
                        value = self.parser.get(section, variable).strip("\"")
                        echo.warning("Variable `" + variable + "` used from section `" + section + "`")
                        return value
                    except configparser.NoOptionError as e:
                        pass
                raise self.NoOptionError
        else:
            return self.parser.get(section, variable).strip("\"")

    def print(self):
        for sec in ["DEFAULT"] + self.parser.sections():
            print("["+ sec +"]")
            for key, value in self.parser.items(sec):
                print(key.upper() + "=\"" + value.strip("\"") + "\"")

    def write(self, filename=None):
        if not filename == None:
            self.filename = filename
        if self.type == "INI":
            self.parser.write(open(self.filename, 'w'))
        elif self.type == "SHELL":
            output = ""
            for sec in ["DEFAULT"] + self.parser.sections():
                for key, value in self.parser.items(sec):
                    output += key.upper() + "=\"" + value.strip("\"") + "\"\n"
            f = file.File(self.filename, 'w')
            f.write(output)
            f.close()
    
    class NoOptionError(Exception):
        pass

