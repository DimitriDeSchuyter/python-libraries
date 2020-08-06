#!/usr/bin/env python3

############################################################################
## LIBRARY for DOCKER Handling                                            ##
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from . import echo, command

import os, sys

# DOCKER EXEC
def exec(flags, container, cmd):
    try:
        Container.exists(container)
    except DockerError as e:
        echo.error(str(e))
        sys.exit(1)
    cmd = "docker exec " + flags + " " + container + " bash -c \"" + cmd.replace("\\","\\\\").replace("\"","\\\"") + "\""
    command.exec(cmd)

# DOCKER CP
def cp(source, destination):
    cmd = "docker cp " + source + " " + destination
    command.exec(cmd)

# DOCKER LOGS
def logs(flags, container):
    try:
        Container.exists(container)
    except DockerError as e:
        echo.error(str(e))
        sys.exit(1)
    cmd = "docker logs " + flags + " " + container
    return command.exec(cmd)

class Container:
    @staticmethod # CONTAINER EXISTS
    def exists(container):
        cmd = "docker ps -q -f name=\"^" + container.replace("\"", "\\\"") + "$\""
        id = len(list(filter(None,command.exec(cmd, False).split("\n"))))
        if id == 0:
            raise DockerError("Container `" + container + "` doesn't exist")
        elif id > 1:
            raise DockerError("Multiple containers matched `" + container + "`")

class Volume:
    @staticmethod # VOLUME EXISTS
    def exists(volume):
        cmd = "docker volume ls -q -f name=\"^" + volume.replace("\"", "\\\"") + "$\""
        id = len(list(filter(None,command.exec(cmd, False).split("\n"))))
        if id == 0:
            raise DockerError("Volume `" + volume + "` doesn't exist")
        elif id > 1:
            raise DockerError("Multiple volumes matched `" + volume + "`")

class Network:
    @staticmethod # NETWORK EXISTS
    def exists(network):
        cmd = "docker network ls -q -f name=\"^" + network.replace("\"", "\\\"") + "$\""
        id = len(list(filter(None,command.exec(cmd, False).split("\n"))))
        if id == 0:
            raise DockerError("Network `" + network + "` doesn't exist")
        elif id > 1:
            raise DockerError("Multiple networks matched `" + network + "`")


class Compose:
    @staticmethod # DOCKER COMPOSE UP
    def up(flags = None, extra = None):
        if flags == None:
            flags = ""
        if extra == None:
            extra = ""
        command.exec("docker-compose up " + flags + " " + extra)

    @staticmethod # DOCKER COMPOSE RUN
    def run(flags, service, cmd = None):
        if flags == None:
            flags = ""
        if cmd == None:
            cmd = ""
        command.exec("docker-compose run " + flags + " " + service + " " + cmd)

    @staticmethod # DOCKER COMPOSE DOWN
    def down(flags = None, extra = None):
        if flags == None:
            flags = ""
        if extra == None:
            extra = ""
        command.exec("docker-compose down " + flags + " " + extra)

    @staticmethod # DOCKER COMPOSE STOP
    def stop(flags = None, extra = None):
        if flags == None:
            flags = ""
        if extra == None:
            extra = ""
        command.exec("docker-compose stop " + flags + " " + extra)

    @staticmethod # DOCKER COMPOSE RESTART
    def restart(flags = None, extra = None):
        if flags == None:
            flags = ""
        if extra == None:
            extra = ""
        command.exec("docker-compose restart " + flags + " " + extra)

    @staticmethod # DOCKER COMPOSE EXEC
    def exec(flags, service, cmd):
        if flags == None:
            flags = ""
        command.exec("docker-compose exec " + flags + " " + service + " " + cmd)

    @staticmethod # DOCKER COMPOSE EXEC BASH
    def bash(flags, service, cmd):
        if flags == None:
            flags = ""
        command.exec("docker-compose exec " + flags + " " + service + " bash -c \"" + cmd.replace("\\","\\\\").replace("\"","\\\"") + "\"")

class DockerError(Exception):
    pass