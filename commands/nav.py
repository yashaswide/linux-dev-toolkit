import os

def goto(args):
    if len(args) < 3:
        print("Usage: ldt goto <folder>")
        return

    try:
        os.chdir(args[2])
        print("Moved to:", os.getcwd())
    except:
        print("Folder not found")

def back():
    os.chdir("..")
    print("Moved to:", os.getcwd())