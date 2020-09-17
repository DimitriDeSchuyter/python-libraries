#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from depuydt import echo

def test_echo():
    echo.notice("Testing notice message")
    echo.warning("Testing warning message")
    echo.error("Testing error message")
    