#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from . import config
import configparser

class Shellconfig(config.Config):

    def read(self):
        self.parser = configparser.ConfigParser()
        self.parser.optionxform=str
        self.parser.read_string('[DEFAULT]\n' + self.handle.read())
    
    def set(self, variable, value):
        try:
            self.parser.set('DEFAULT', variable, "\"" + value + "\"")            
        except (configparser.NoSectionError) as e:
            self.parser.add_section('DEFAULT')
            self.parser.set('DEFAULT', variable, "\"" + value + "\"")
        return value

    def get(self, variable, default = None):
        try:
            return self.parser.get('DEFAULT', variable).strip("\"")
        except configparser.NoOptionError as e:
            if not default == None: return default 
            else: raise KeyError(e)
            
    def write(self):
        self.clear()
        for key, value in self.parser.items('DEFAULT'):
            super().write(key + "=" + value + "\n")

    def print(self):
        for key, value in self.parser.items('DEFAULT'):
            print(" " + key + " = " + value.strip("\"")) 
