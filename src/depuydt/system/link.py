#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from .. import command, directory, echo, file
import os

class Link:

    @staticmethod
    def get(path: str):
        path = str(path)
        if os.path.islink(path):
            return path
        path = os.path.expanduser(path)
        if os.path.islink(path):
            return path
        else:
            return None

    @staticmethod
    def exists(path: str):
        return Link.get(path) is not None

    @staticmethod
    def target(path: str):
        path = Link.get(path)
        if path is not None:
            return os.readlink(path)
        else:
            return None

    @staticmethod
    def create(path: str, target: str):
        path = str(path)
        target = str(target)

        ## check if target exists
        if not directory.exists(target):
            if not file.exists(target):
                raise FileNotFoundError(target)
            else:
                target = file.get(target)
        else:
            target = directory.get(target)

        ## check if path doesn't already exists
        if Link.exists(path):
            if Link.target(path) == target:
                return Link(path)
            else:
                raise FileNotFoundError(path) #is already another link ERROR
        elif directory.exists(path) or file.exists(path):
            raise FileNotFoundError(path) #is already another file ERROR
        else:
            os.symlink(target, path)
            return Link(path)
  
    def __init__(self, path: str):
        self.path = path
        self.target = self._instance_of_target

    def __str__(self):
        return str(self.path)

    def _instance_of_target(self):
        return Link.target(self.path)

    def remove(self):
        os.unlink(self.path)
        del self
