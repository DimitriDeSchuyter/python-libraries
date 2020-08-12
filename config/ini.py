#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################
from .. import echo
from . import config

import configparser


class Iniconfig(config.Config):
    def read(self):
        self.parser = configparser.ConfigParser(allow_no_value=True)
        self.parser.optionxform=str
        try:
            self.parser.read_file(self.handle)
        except configparser.ParsingError as e:
            echo.error("Parsing error: " + str(e))
            exit(1)
        self.section = 'DEFAULT'

    def set(self, variable, value):
        try:
            self.parser.set(self.section, variable, value)
        except (configparser.NoSectionError) as e:
            self.parser.add_section(self.section)
            self.parser.set(self.section, variable, value)

    def get(self, variable, default = None):  
        try:
            return self.parser.get(self.section, variable).strip("\"")
        except configparser.NoOptionError as e:
            if not default == None: return default 
            else: raise KeyError(e)

    def write(self):
        self.clear()
        self.parser.write(self.handle)

    def print(self):
        for section in self.parser.sections():
            print("["+ section +"]")
            for key, value in self.parser.items(section):
                print(" " + key + " = " + value.replace("\n"," ")) 