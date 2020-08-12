#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from .. import echo, file
#from . import ini, json, shell

class Config(file.File):

    mode = "r+"

    def __init__(self, path):
        super().__init__(path, self.mode)
        self.read()

    def require(self, variable, default = None):
        try:
            # Check whether the variable is already declared in the file
            return self.get(variable)
        except KeyError as e:
            # Prompt the user for the variable and write it direcly in the file
            return self.set(variable, default if not default == None else echo.prompt(variable))

    def save(self):
        self.write()
        self.close()

    def print(self):
        for sec in ["DEFAULT"] + self.parser.sections():
            print("["+ sec +"]")
            for key, value in self.parser.items(sec):
                print(key.upper() + "=\"" + value.strip("\"") + "\"")

    class NoOptionError(Exception):
        pass