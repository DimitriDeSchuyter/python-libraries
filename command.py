#!/usr/bin/env python3

############################################################################
## LIBRARY for COMMAND Handling                                           ##
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from . import echo
import os

# CMD EXECUTE
def exec(cmd, verbose = True):
    if __debug__:
        echo.debug(cmd)
    result = os.popen(cmd).read()
    if verbose:
        print(result)
    return result