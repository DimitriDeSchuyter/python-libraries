#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from depuydt.system import link

def test_file():
    assert link.exists("non-existing-file") == False
    assert link.exists("tests") == True
    