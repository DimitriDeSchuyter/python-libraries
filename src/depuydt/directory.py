#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from . import echo
import os

def get(path: str):
    path = str(path)
    if os.path.isdir(path):
        return path
    path = os.path.expanduser(path)
    if os.path.isdir(path):
        return path
    else:
        return None

def exists(path: str):
    return get(path) is not None

def create(path):
    try:
        os.mkdir(path)
        return Directory(path)
    except FileExistsError as e:
        echo.warning("Directory exists: " + str(e))
        return Directory(path)

class Directory():

    path = ""

    def __init__(self, path):
        self.path = path
        if not os.path.isdir(path):
            raise FileNotFoundError(path)

    def __str__(self):
        return str(self.path)

    
