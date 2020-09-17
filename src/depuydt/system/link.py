#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from .. import command, directory, echo, file


def exists(path: str):
    if directory.exists(path):
        return True
    if file.exists(path):
        return True
    return False

def symbolic(src: str, dst: str):
    if directory.exists(src):
        if not directory.exists(dst):
            pass
            #command.exec("ln -s " + src + " " + dst)
        else:
            echo.warning("Destination is already a folder")
    else:
        echo.error("Source isn't a folder")