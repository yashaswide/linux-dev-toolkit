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


def show(args):
    items = os.listdir()

    files = []
    dirs = []

    for item in items:
        if os.path.isdir(item):
            dirs.append(item)
        else:
            files.append(item)

    # --- FLAGS ---
    show_files = "--files" in args
    show_dirs = "--dirs" in args

    # If no flags → show everything
    if not show_files and not show_dirs:
        show_files = True
        show_dirs = True

    print()

    if show_files:
        print("📁 Files:")
        for f in files:
            print(" -", f)

    if show_dirs:
        print("\n📂 Directories:")
        for d in dirs:
            print(" -", d)

    print("\n📊 Summary:")
    print("Files:", len(files))
    print("Directories:", len(dirs))

def where():
    print(os.getcwd())

def make(args):
    base_path = os.path.expanduser("~/Desktop")
    if len(args) < 3:
        print("Usage: ldt make <folder> [file]")
        return
    folder = args[2]
    folder_path = os.path.join(base_path, folder)
    # 1. Create folder
    os.makedirs(folder_path, exist_ok=True)
    print("folder name:", folder)
    print("folder path:", folder_path)
    # 2. Create file ONLY if provided
    if len(args) > 3:
        file = args[3]
        file_path = os.path.join(folder_path, file)
        with open(file_path, "w") as f:
            pass  # creates empty file
        print("file name:", file)
        print("file path:", file_path)

BASE_PATH = os.path.expanduser("~/Desktop")
def find_target(name):
    for root, dirs, files in os.walk(BASE_PATH):
        if name in files:
            return os.path.join(root, name)
        if name in dirs:
            return os.path.join(root, name)
    return None

def rename(args):
    if len(args) < 4:
        print("Usage: ldt rename <old_name> <new_name>")
        return
    old_name = args[2]
    new_name = args[3]
    base_path = os.path.expanduser("~/Desktop")
    old_path = None
    # search file in Desktop tree
    for root, dirs, files in os.walk(base_path):
        if old_name in files:
            old_path = os.path.join(root, old_name)
            break
    if not old_path:
        print("File not found")
        return
    new_path = os.path.join(os.path.dirname(old_path), new_name)
    try:
        os.rename(old_path, new_path)
        print(f"RENAMED: {old_name} → {new_name}")
        print("path:", new_path)
    except Exception as e:
        print("Error:", e)

def rename_folder(args):
    if len(args) < 4:
        print("Usage: ldt rename-folder <old_folder> <new_folder>")
        return
    old_name = args[2]
    new_name = args[3]
    base_path = os.path.expanduser("~/Desktop")
    old_path = None
    # search folder inside Desktop tree
    for root, dirs, files in os.walk(base_path):
        if old_name in dirs:
            old_path = os.path.join(root, old_name)
            break
    if not old_path:
        print("Folder not found")
        return
    new_path = os.path.join(os.path.dirname(old_path), new_name)
    try:
        os.rename(old_path, new_path)
        print(f"RENAMED folder: {old_name} → {new_name}")
        print("path:", new_path)
    except Exception as e:
        print("Error:", e)

def delete(args):
    if len(args) < 3:
        print("Usage: ldt delete <file/folder>")
        return
    target_name = args[2]
    target_path = find_target(target_name)
    if not target_path:
        print("File/folder not found")
        return
    confirm = input(f"Are you sure you want to delete '{target_name}'? (y/n): ")
    if confirm.lower() != "y":
        print("Cancelled")
        return
    try:
        if os.path.isfile(target_path):
            os.remove(target_path)
        else:
            shutil.rmtree(target_path)
        print(f"Deleted '{target_name}'")
    except Exception as e:
        print("Error:", e)

def clear():
    os.system("cls" if os.name == "nt" else "clear")