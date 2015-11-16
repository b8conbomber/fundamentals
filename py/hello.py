#!/usr/bin/env python3

"""Not you grans hello world"""

import skilstak.colors as c
import time

def plain(message):
    print(c.cl + c.x +message)

def color(message):
    print(c.cl,end="")
    while True:
        print(c.rc() + message + c.x, end=" ")

def multi(message):
    """Mulit Colord"""
    while True:
        print(c.cl + c.multi(message))
        time.sleep(0.5)

if __name__ == "__main__":
    import sys
    
    who = "World"
    option = ""
    message = ""

    if len(sys.argv) > 2:
        option = sys.argv[1]
        who = sys.argv[2]
    elif len(sys.argv) == 2:
        if sys.argv[1].startswith("-"):
            option = sys.argv[1]
        else:
            who = sys.argv[1]

    message = "Hello, " + who + "!"

    try:
        if option == "-c":
            color(message)
        elif option == "-m":
            multi(message)
        else:
            plain(message)
    except KeyboardInterrupt:
        exit(0)
