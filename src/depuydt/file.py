#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from . import echo
import os, shutil
from errno import ENOENT, EACCES, EPERM

def get(path: str):    
    path = str(path)
    if os.path.exists(path):
        return path
    path = os.path.expanduser(path)
    if os.path.exists(path):
        return path
    else:
        return None

def exists(path: str):
    return get(path) is not None

def create(path: str):
    try:
        open(path, "w+").close()
        return File(path)
    except FileExistsError as e:
        echo.warning("File exists: " + str(e))
        return File(path)


def copy(src, dst):
    try:
        shutil.copyfile(src, dst)
    except Exception as e:
        echo.error(str(e))
        raise

def append(src, dst):
    try:
        fin = File(src, "r")
        data2 = fin.read()
        fin.close()
        fout = File(dst, "a")
        fout.write(data2)
        fout.close()
    except Exception as e:
        echo.error(str(e))
        raise
    
class File:

    path = ""
    mode = "r"

    # CONSTRUCTOR
    def __init__(self, path, mode = "r"):
        self.path = str(path)
        self.setMode(mode)
        self.exists()
        self.open()

    def __str__(self):
        return str(self.path)

    def setMode(self, mode):
        self.mode = mode

    def exists(self):
        if os.path.exists(self.path):
            return True
        self.path = os.path.expanduser(self.path)
        return os.path.exists(self.path)

    def open(self):
        self.handle = open(self.path, self.mode)

    def read(self):
        self.content = self.handle.read()
        return self.content

    def seek(self, pointer):
        return self.handle.seek(pointer)

    def truncate(self, size=None):
        if size == None:
            return self.handle.truncate()
        else:
            return self.handle.truncate(size)

    def clear(self):
        self.seek(0)
        self.truncate()

    def write(self, content = None):
        if not content == None:
            self.content = str(content)
        self.handle.write(self.content)
        return True

    def close(self):
        self.handle.close()
        return True