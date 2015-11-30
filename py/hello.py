#!/usr/bin/env python3

"""Not you grans hello world"""

import skilstak.colors as c
import time

def print_plain(message):
    print(c.cl + c.x +message)

def print_color(message):
    print(c.cl,end="")
    while True:
        print(c.rc() + message + c.x, end=" ")

def print_multi(message):
    """Mulit Colord"""
    while True:
        print(c.cl + c.multi(message))
        time.sleep(0.5)

def parse_args():
    from sys import argv
    
    name = "World"
    option = ""

    if len(argv) > 2:
        option = argv[1]
        name = argv[2]
    elif len(argv) == 2:
        if argv[1].startswith("-"):
           option = argv[1]
        else:
            name = argv[1]

    return name, option
