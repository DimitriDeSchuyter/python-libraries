#!/usr/bin/env python3

############################################################################
## LIBRARY for Directory Handling                                         ##
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from echo import echo
import os

class directory:

    @staticmethod # DIRECTORY CREATE
    def create(path):
        try:
            os.mkdir(path);
        except FileExistsError as e:
            echo.notice("Directory exists: " + str(e));
