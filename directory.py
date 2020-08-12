#!/usr/bin/env python3

############################################################################
## LIBRARY for Directory Handling                                         ##
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from . import echo
import os

from pprint import pprint

class Directory():

    path = ""

    def __init__(self, path):
        self.path = path
        if not os.path.isdir(path):
            raise FileNotFoundError(path)

    def __str__(self):
        return str(self.path)

    @staticmethod # DIRECTORY CREATE
    def create(path):
        try:
            os.mkdir(path)
        except FileExistsError as e:
            echo.notice("Directory exists: " + str(e))
