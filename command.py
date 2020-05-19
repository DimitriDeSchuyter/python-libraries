#!/usr/bin/env python3

############################################################################
## LIBRARY for COMMAND Handling                                           ##
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from echo import echo;
import os;

class command:

    @staticmethod # CMD EXECUTE
    def exec(cmd, verbose = True):
        if __debug__:
            echo.debug(cmd);
        try:
            if verbose:
                os.system(cmd);
            else:
                return os.popen(cmd).read();
        except Exception as e:
            echo_error("command exec: " + str(e));
            exit(1);

if __debug__:
    echo.debug("imported `command.py`");