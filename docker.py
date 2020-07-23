#!/usr/bin/env python3

############################################################################
## LIBRARY for DOCKER Handling                                            ##
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from echo import echo;
from command import command;
import os, sys;

class docker:

    @staticmethod # DOCKER EXEC
    def exec(flags, container, cmd):
        try:
            docker.container.exists(container);
        except dockerError as e:
            echo.error(str(e));
            sys.exit(1);
        cmd = "docker exec " + flags + " " + container + " bash -c \"" + cmd.replace("\\","\\\\").replace("\"","\\\"") + "\""; 
        command.exec(cmd);

    @staticmethod # DOCKER CP
    def cp(source, destination):
        cmd = "docker cp " + source + " " + destination;
        command.exec(cmd);

    @staticmethod # DOCKER LOGS
    def logs(flags, container):
        try:
           docker.container.exists(container);
        except dockerError as e:
            echo.error(str(e));
            sys.exit(1);
        cmd = "docker logs " + flags + " " + container;
        return command.exec(cmd);

    class container:
        @staticmethod # CONTAINER EXISTS
        def exists(container):
            cmd = "docker ps -q -f name=\"^" + container.replace("\"", "\\\"") + "$\"";
            id = len(list(filter(None,command.exec(cmd, False).split("\n"))));
            if id == 0:
                raise dockerError("Container `" + container + "` doesn't exist");
            elif id > 1:
                raise dockerError("Multiple containers matched `" + container + "`");

    class volume:
        @staticmethod # VOLUME EXISTS
        def exists(volume):
            cmd = "docker volume ls -q -f name=\"^" + volume.replace("\"", "\\\"") + "$\"";
            id = len(list(filter(None,command.exec(cmd, False).split("\n"))));
            if id == 0:
                raise dockerError("Volume `" + volume + "` doesn't exist");
            elif id > 1:
                raise dockerError("Multiple volumes matched `" + volume + "`");

    class network:
        @staticmethod # NETWORK EXISTS
        def exists(network):
            cmd = "docker network ls -q -f name=\"^" + network.replace("\"", "\\\"") + "$\"";
            id = len(list(filter(None,command.exec(cmd, False).split("\n"))));
            if id == 0:
                raise dockerError("Network `" + network + "` doesn't exist");
            elif id > 1:
                raise dockerError("Multiple networks matched `" + network + "`");


    class compose:
        @staticmethod # DOCKER COMPOSE UP
        def up(flags = None, extra = None):
            if flags == None:
                flags = "";
            if extra == None:
                extra = "";
            command.exec("docker-compose up " + flags + " " + extra);

        @staticmethod # DOCKER COMPOSE RUN
        def run(flags, service, cmd = None):
            if flags == None:
                flags = "";
            if cmd == None:
                cmd = "";
            command.exec("docker-compose run " + flags + " " + service + " " + cmd);

        @staticmethod # DOCKER COMPOSE DOWN
        def down(flags = None, extra = None):
            if flags == None:
                flags = "";
            if extra == None:
                extra = "";
            command.exec("docker-compose down " + flags + " " + extra);

        @staticmethod # DOCKER COMPOSE STOP
        def stop(flags = None, extra = None):
            if flags == None:
                flags = "";
            if extra == None:
                extra = "";
            command.exec("docker-compose stop " + flags + " " + extra);

        @staticmethod # DOCKER COMPOSE RESTART
        def restart(flags = None, extra = None):
            if flags == None:
                flags = "";
            if extra == None:
                extra = "";
            command.exec("docker-compose restart " + flags + " " + extra);

        @staticmethod # DOCKER COMPOSE EXEC
        def exec(flags, service, cmd):
            if flags == None:
                flags = "";
            command.exec("docker-compose exec " + flags + " " + service + " " + cmd);

        @staticmethod # DOCKER COMPOSE EXEC BASH
        def bash(flags, service, cmd):
            if flags == None:
                flags = "";
            command.exec("docker-compose exec " + flags + " " + service + " bash -c \"" + cmd.replace("\\","\\\\").replace("\"","\\\"") + "\""); 

class dockerError(Exception):
    pass


if __debug__:
    echo.debug("imported `docker.py`");
