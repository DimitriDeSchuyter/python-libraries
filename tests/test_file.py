#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from depuydt import file

def test_file():
    assert file.exists("non-existing-file") == False
    assert file.exists("tests/test_file.py") == True
    