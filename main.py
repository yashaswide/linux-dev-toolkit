import sys
from commands import nav

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
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()