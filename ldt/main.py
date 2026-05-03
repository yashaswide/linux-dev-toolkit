#!/usr/bin/env python3
import sys
import os
#sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ldt.commands import nav
from ldt.commands import help_cmd
from ldt.commands import parser

def main():
    args = sys.argv

    if len(args) < 2:
        print("Usage: ldt <command>")
        return

    cmd = args[1]
    if cmd == "goto":
        nav.goto(args)
    elif cmd == "back":
        nav.back()
    elif cmd == "show":
        nav.show(args)
    elif cmd == "where":
        nav.where()
    elif cmd == "make":
        nav.make(args)
    elif cmd == "delete":
        nav.delete(args)
    elif cmd == "clear":
        nav.clear()
    elif cmd == "help":
        help_cmd.show_help(args)
    elif cmd == "version":
        print("LDT v0.1")
    elif cmd == "run":
        parser.run_sentence(" ".join(args[2:]))
    elif cmd == "rename":
        nav.rename(args)
    elif cmd == "rename-folder":
        nav.rename_folder(args)
    elif cmd == "head":
        nav.head(args)
    elif cmd == "tail":
        nav.tail(args)
    elif cmd == "shutdown":
        nav.shutdown()
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()