#!/usr/bin/env python3
import sys
import os
#sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ldt.commands import nav
from ldt.commands import help_cmd
from ldt.commands import parser

VERSION = "0.1.0"

def show_header():
    path = os.getcwd()
    home = os.path.expanduser("~")
    if path.startswith(home):
        path = path.replace(home, "~")
    print(f"\nLDT v{VERSION} | {path}")
    print("-" * 40)



def run_command(args):
    if len(args) < 2:
        print("Usage: ldt <command>")
        return

    cmd = args[1]
    if cmd == "goto":
        nav.goto(["ldt"] + args)
    elif cmd == "back":
        nav.back()
    elif cmd == "show":
        nav.show(["ldt"] + args)
    elif cmd == "where":
        nav.where()
    elif cmd == "make":
        nav.make(["ldt"] + args)
    elif cmd == "delete":
        nav.delete(["ldt"] + args)
    elif cmd == "clear":
        nav.clear()
    elif cmd == "help":
        help_cmd.show_help(["ldt"] + args)
    elif cmd == "version":
        print("LDT v0.1")
    elif cmd == "run":
        parser.run_sentence(" ".join(args[2:]))
    elif cmd == "rename":
        nav.rename(["ldt"] + args)
    elif cmd == "rename-folder":
        nav.rename_folder(["ldt"] + args)
    elif cmd == "head":
        nav.head(["ldt"] + args)
    elif cmd == "tail":
        nav.tail(["ldt"] + args)
    elif cmd == "shutdown":
        nav.shutdown()
    else:
        print("Unknown command")

def interactive_mode():
    show_header()
    while True:
        try:
            user_input = input("ldt > ").strip()
            if not user_input:
                continue
            if user_input in ["exit", "quit"]:
                print("Exiting LDT...")
                break
            args = user_input.split()
            run_command(args)
        except KeyboardInterrupt:
            print("\nUse 'exit' to quit.")
        except Exception as e:
            print("Error:", e)


def main():
    args = sys.argv
    # If only `ldt` → interactive mode
    if len(args) == 1:
        interactive_mode()
        return
    # Otherwise normal CLI mode
    cmd_args = args[1:]
    run_command(cmd_args)

if __name__ == "__main__":
    main()