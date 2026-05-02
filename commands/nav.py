import os
import shutil
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

def show():
    files = os.listdir()
    for f in files:
        if os.path.isdir(f):
            print(f"[DIR]  {f}")
        else:
            print(f"       {f}")

def where():
    print(os.getcwd())

def make(args):
    if len(args) < 3:
        print("Usage: ldt make <folder_name>")
        return

    folder = args[2]

    try:
        os.mkdir(folder)
        print(f"Folder '{folder}' created")
    except FileExistsError:
        print("Folder already exists")
    except Exception as e:
        print("Error:", e)

def delete(args):

    if len(args) < 3:

        print("Usage: ldt delete <file/folder>")

        return

    target = args[2]

    if not os.path.exists(target):

        print("File/folder not found")

        return

    confirm = input(f"Are you sure you want to delete '{target}'? (y/n): ")

    if confirm.lower() != "y":

        print("Cancelled")

        return

    try:

        if os.path.isfile(target):

            os.remove(target)

        else:

            shutil.rmtree(target)

        print(f"Deleted '{target}'")

    except Exception as e:

        print("Error:", e)

def clear():
    os.system("cls" if os.name == "nt" else "clear")