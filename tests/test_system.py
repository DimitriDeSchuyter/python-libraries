#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from depuydt import directory, file
from depuydt.system import Link
import tempfile, os, shutil

def test_system():
    ## Checking directory library
    d = tempfile.mkdtemp()
    assert directory.exists(d) == True
    assert directory.exists(d + "/non-existing-dir") == False
    D = directory.Directory(d)    
    assert directory.exists(D) == True
    D = directory.create(d + "/dir")
    assert directory.exists(D) == True

    ## Checking file library
    f = tempfile.mkstemp(dir=d)[1]
    assert file.exists(f) == True
    assert file.exists(d + "/non-existing-file") == False
    F = file.File(f)    
    assert file.exists(D) == True
    F = file.create(d + "/file")
    assert file.exists(D) == True

    ## Checking link library
    l = os.symlink(f, d + "/link")
    assert Link.exists(d + "/link") == True
    assert Link.exists(d + "/non-existing-link") == False

    L = Link(d + "/link")    
    assert Link.exists(L) == True
    assert file.exists(L.target()) == True
    L.remove()

    L = Link.create(d + "/link", f)
    assert Link.exists(L) == True
    assert file.exists(L.target()) == True

    shutil.rmtree(d)

