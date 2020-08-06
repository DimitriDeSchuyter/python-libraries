#!/usr/bin/env python3

############################################################################
## LIBRARY for File Handling                                              ##
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from . import echo
import os
from errno import ENOENT, EACCES, EPERM

CREATE_IF_NOT_EXISTS = False

class File:   

    # CONSTRUCTOR
    def __init__(self, path, mode):
        self.path = str(path);
        self.mode = str(mode);
        self.open();

    def exists(self):
        if os.path.exists(self.path):
            return True
        try:
            self.path = os.path.expanduser(self.path)
            return os.path.exists(self.path)
        except Exception as e:
            echo.error(str(e))
            raise

    def open(self):
        try:
            if not self.exists():
                if CREATE_IF_NOT_EXISTS:
                    self.handle = open(self.path, "w+")    
                else:
                    echo.error("File doesn't exist: " + self.path)
                    exit(1)
            else:
                self.handle = open(self.path, self.mode)
        except Exception as e:
            echo.error(str(e))
            raise


    def write(self, text):
        try:
            self.handle.write(str(text))            
            return True
        except Exception as e:
            echo.error(str(e))
            raise

    def read(self):
        try:
            return self.handle.read()
        except Exception as e:
            echo.error(str(e))
            raise

    def close(self):
        try:
            self.handle.close()
            return True
        except Exception as e:
            echo.error(str(e))
            raise