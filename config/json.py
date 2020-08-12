#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from . import config

import json

class Jsonconfig(config.Config):
    def read(self):
        if super().read() == "":
            self.content = "{}"
        self.json = json.loads(self.content)

    def get(self, variable, default = None):
        try:
            return self.json[variable]
        except KeyError as e:
            if not default == None: return default
            else: raise e

    def set(self, variable, value):
        self.json[variable] = value

    def write(self):
        self.clear()
        super().write(json.dumps(self.json))

    def print(self):
        pass
