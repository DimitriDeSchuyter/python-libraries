#!/usr/bin/env python3

############################################################################
## LIBRARY for ECHO Handling                                              ##
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from color import color

class echo:
    # CONSTRUCTOR
    def __init__(self, text):
        echo.warning("Unnecessary use of echo class, use print instead");
        print(text);

    @staticmethod # TITLE BLOCK
    def title(title):
        title = str(title);
        width   = 100;
        w_space = width - 10 - len(title);
        w_left  = int(w_space / 2);
        w_right = int(w_space - w_left);
        title   = (" " * w_left) + color.cyan + title + color.default + (" " * w_right);
        print("");
        print(color.red + ("*" * width) + color.default);
        print(color.red + "*****" + color.default + title + color.red + "*****" + color.default);
        print(color.red  + ("*" * width) + color.default);


    @staticmethod # SECTION LINE
    def section(section, text, col = color.cyan):
        section = str(section);
        text = str(text);
        if section is None:
            print(col + text + color.default);
        else:
            print(col + section + ": " + color.default + text);

    @staticmethod # COMMENT LINE
    def comment(text):
        echo.section(None, text, color.green);

    @staticmethod # COMMENT LINE
    def notice(text):
        echo.section(" NOTICE", text, color.green);

    @staticmethod # WARNING LINE
    def warning(text):
        echo.section(" WARNING", text, color.yellow);

    @staticmethod # ERROR LINE
    def error(text):
        echo.section(" ERROR", text, color.red);

    @staticmethod # DEBUG LINE
    def debug(text):
        echo.section(" DEBUG", text, color.purple);

    @staticmethod # PROMPT LINE
    def prompt(variable, password = False):
        echo.section(" PROMPT", variable + " = ", color.green);
        return input("");

if __debug__:
    echo.debug("imported `echo.py`");

