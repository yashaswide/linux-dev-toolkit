#!/usr/bin/env python3
import sys
import os
#sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ldt.commands import nlm
from ldt.commands import nav
from ldt.commands import help_cmd
from ldt.commands import parser
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
try:
    import gnureadline as readline
except ImportError:
    import readline

COMMANDS = [
    "goto", "back", "show", "where", "head", "tail",
    "rename", "delete", "help", "clear", "exit", "shutdown",
    "rename-folder", "make"
]

def completer(text, state):
    buffer = readline.get_line_buffer()
    tokens = buffer.split()

    if len(tokens) <= 1:
        matches = [cmd for cmd in COMMANDS if cmd.startswith(text)]
    else:
        matches = []

    return matches[state] if state < len(matches) else None

if readline:
    readline.set_completer(completer)
    readline.parse_and_bind("tab: complete")
    readline.set_completer_delims(" \t\n;")
VERSION = "0.1.0"

def show_header():
    path = os.getcwd()
    home = os.path.expanduser("~")
    if path.startswith(home):
        path = path.replace(home, "~")
    print(f"\nLDT v{VERSION} | {path}")
    print("-" * 40)



def run_command(args):
    if len(args) < 1:
        print("Usage: ldt <command>")
        return

    cmd = args[0]
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
        if len(args) < 2:
            print("Usage: run <sentence>")
            return
        sentence = " ".join(args[1:]).strip()
        result = nlm.understand(sentence)
        intent = result["intent"]
        file = result["file"]
        folder = result["folder"]
        number = result["number"]

         # -------------------------
        # TAIL
        # -------------------------
        if intent == "tail" and file:
            nav.tail([
                "ldt",
                "tail",
                file,
                str(number or 10)
            ])

         # -------------------------
         # HEAD
         # -------------------------
        elif intent == "head" and file:
            nav.head([
             "ldt",
             "head",
             file,
             str(number or 10)
         ])

        # -------------------------
        # DELETE
        # -------------------------
        elif intent == "delete":
            target = file if file else folder
            if target:
               nav.delete([
                  "ldt",
                  "delete",
                  target
             ])
            else:
                print("Couldn't determine target")
        else:
            print("Unsupported sentence")
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



COMMAND_COMPLETER = WordCompleter(COMMANDS)


def interactive_mode():
    show_header()

    while True:
        try:
            user_input = prompt("ldt > ", completer=COMMAND_COMPLETER)

            if not user_input.strip():
                continue

            if user_input in ["exit", "quit"]:
                print("Exiting LDT...")
                break

            args = user_input.split()

            # -------------------------
           # NORMAL COMMAND
           # -------------------------
            if args[0] in COMMANDS:
                run_command(args)

            # -------------------------
            # NATURAL LANGUAGE MODE
            # -------------------------
            else:

                result = nlm.understand(user_input)

                intent = result["intent"]
                file = result["file"]
                folder = result["folder"]
                number = result["number"]

                # -------------------------
                # SHOW FILES
                # -------------------------
                if intent == "show":
                     nav.show(["ldt", "show"])

                    # -------------------------
                    # HEAD
                    # -------------------------
                elif intent == "head" and file:
                    nav.head([
                    "ldt",
                    "head",
                    file,
                    str(number or 10)
                ])
  
                   # -------------------------
                   # TAIL
               # -------------------------
                elif intent == "tail" and file:
                   nav.tail([
                  "ldt",
                  "tail",
                  file,
                 str(number or 10)
                ])

                 # -------------------------
                # DELETE
                # -------------------------
                elif intent == "delete":

                    target = file if file else folder
 
                    if target:
                       nav.delete([
                       "ldt",
                       "delete",
                       target
                    ])
                    else:
                         print("Couldn't determine target")

                # -------------------------
                # CREATE FOLDER
                # -------------------------
                elif intent == "create" and folder:

                     nav.make([
                     "ldt",
                     "make",
                     folder
                    ])

                else:
                    print("Sorry, I couldn't understand.")
            

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