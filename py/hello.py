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
    import sys
    
    p = {
        "who": "World",
        "option": ""
    }

    if len(sys.argv) > 2:
        p["option"] = sys.argv[1]
        p["who"] = sys.argv[2]
    elif len(sys.argv) == 2:
        if sys.argv[1].startswith("-"):
           p["option"] = sys.argv[1]
        else:
            p["who"] = sys.argv[1]

    return p
