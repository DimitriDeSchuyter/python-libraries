#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from depuydt import directory

def test_directory():
    assert directory.exists("non-existing-directory") == False
    assert directory.exists("tests") == True
    