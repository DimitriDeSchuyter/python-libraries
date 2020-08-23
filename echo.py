#!/usr/bin/env python3

############################################################################
## LIBRARY for ECHO Handling                                              ##
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from . import color

flush = False

def setFlush(value):
    global flush
    flush = value

# TITLE BLOCK
def title(title):
    global flush
    title = str(title)
    width   = 100
    w_space = width - 10 - len(title)
    w_left  = int(w_space / 2)
    w_right = int(w_space - w_left)
    title   = (" " * w_left) + color.cyan + title + color.default + (" " * w_right)
    print("", flush)
    print(color.red + ("*" * width) + color.default, flush)
    print(color.red + "*****" + color.default + title + color.red + "*****" + color.default, flush)
    print(color.red  + ("*" * width) + color.default, flush)

# SECTION LINE
def section(section, text, col = color.cyan):
    global flush
    section = str(section)
    text = str(text)
    if section is None:
        print(col + text + color.default, flush)
    else:
        print(col + section + color.default +  ": " + text, flush)

# COMMENT LINE
def comment(text):
    section(None, text, color.green)

# COMMENT LINE
def notice(text):
    section("NOTICE", text, color.green)

# WARNING LINE
def warning(text):
    section("WARNING", text, color.yellow)

# ERROR LINE
def error(text):
    section("ERROR", text, color.red)

# DEBUG LINE
def debug(text):
    section("DEBUG", text, color.purple)

# PROMPT LINE
def prompt(variable, password = False):
    section("PROMPT", variable + " = ", color.green)
    return input("")