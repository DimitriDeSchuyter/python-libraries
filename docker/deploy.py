#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from .. import config, directory, docker, echo, file
import os, sys

from pprint import pprint


class Deploy():

    def __init__(self):
        self.cwd = os.getcwd() # Current Work Directory
        try:
            self.dwd = directory.Directory(self.cwd + "/.docker-deploy")
            sys.path.append(str(self.dwd))
        except FileNotFoundError as e:
            echo.error("Current work directory has no .docker-deploy folder")
            exit(1)


        try:
            self.dcf = file.File(self.cwd + "/docker-compose.yml")
        except FileNotFoundError as e:
            echo.error("Current work directory has no docker-compose.yml file")
            exit(1)

        try:
            f = file.File(str(self.dwd) + "/config.json")
        except FileNotFoundError as e:
            try:
                f = file.File(str(self.dwd) + "/config.json.example")
                file.copy(str(self.dwd) + "/config.json.example", str(self.dwd)+ "/config.json")
            except FileNotFoundError as e:
                echo.warning(".docker-deploy directory didn't contain a valid configuration file")

        self.config = config.Jsonconfig(str(self.dwd) + "/config.json")
        self.name = self.config.get("name","<TITLE PLACEHOLDER>")
        self.state = self.config.get("state", 0)
        self.auto()

    def auto(self):
        try:
            while(not self.run()): self.state += 1
        except Exception as e:
            self.config.set("state", self.state)
            self.config.save()
            echo.error(str(e))
            exit(1)

    def run(self):
        if(self.state == 0):
            return self.pull()
        elif(self.state == 1):
            return self.build()
        elif(self.state == 2):
            return self.create()
        elif(self.state == 3):
            return self.preconf()
        elif(self.state == 4):
            return self.start()
        elif(self.state == 5):
            return self.postconf()
        else:
            raise Exception("State ran out of bounds")                

    def pull(self):
        self.echoTitle("Pulling images")
        docker.Compose.pull("--include-deps")

    def build(self):
        self.echoTitle("Building images")
        docker.Compose.build("--no-cache")

    def create(self):
        self.echoTitle("Creating containers")
        docker.Compose.up("--no-start --force-recreate")

    def preconf(self):
        if file.exists(str(self.dwd) + "/pre.py"):
            self.echoTitle("Applying pre-configuration")
            import pre

    def start(self):
        self.echoTitle("Starting containers")
        docker.Compose.up("--detach")

    def postconf(self):
        if file.exists(str(self.dwd) + "/post.py"):
            self.echoTitle("Applying post-configuration")
            import post

    def echoTitle(self,status):
        echo.section("DOCKER DEPLOYING", self.name + " (" + status + ")")


