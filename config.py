#!/usr/bin/env python3

############################################################################
## LIBRARY for File Handling                                              ##
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from echo import echo
import configparser
from pprint import pprint

class config:    
    

    def __init__(self, filename, configtype = "INI"):
        self.filename = filename;
        self.type = configtype;        
        self.parser = None;
        self.read();

    def read(self):
        if self.type == "SHELL":
            config_str = '[DEFAULT]\n' + open(self.filename, 'r').read();
            self.parser = configparser.ConfigParser();
            self.parser.read_string(config_str);
        elif self.type == "INI":
            self.parser = configparser.ConfigParser();
            self.parser.read(self.filename);
        else:
            raise Exception("Config type unsupported");       

    def set(self, section, variable, value):
        try:            
            self.parser.set(section, variable, value);            
        except Exception as e:
            echo.error(str(e));
            exit(1);

    def get(self, section, variable):
        if section == None:
            try:
                return self.parser.get("DEFAULT", variable).strip("\"");
            except (configparser.NoSectionError, configparser.NoOptionError) as e:
                for section in self.parser.sections():
                    try:
                        value = self.parser.get(section, variable).strip("\"");
                        echo.warning("Variable `" + variable + "` used from section `" + section + "`");
                        return value;
                    except configparser.NoOptionError as e:
                        pass;
                raise configparser.NoOptionError;
        else:
            return self.parser.get(section, variable).strip("\"");

    def print(self):
        for sec in ["DEFAULT"] + self.parser.sections():
            for key, value in self.parser.items(sec):
                print(key.upper() + "=\"" + value.strip("\"") + "\"");

    def write(self, filename=None):
        if not filename == None:
            self.filename = filename;
        if self.type == "INI":
            self.parser.write(self.filename);
        elif self.type == "SHELL":
            output = "";
            for sec in ["DEFAULT"] + self.parser.sections():
                for key, value in self.parser.items(sec):
                    output += key.upper() + "=\"" + value.strip("\"") + "\"\n";
            open(self.filename, 'w').write(output);

