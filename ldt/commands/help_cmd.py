help_data = {
    "goto": "Change directory\nUsage: ldt goto <folder>",
    "back": "Go to parent directory\nUsage: ldt back",
    "show": "List files\nUsage: ldt show",
    "where": "Show current directory\nUsage: ldt where",
    "make": "Create folder\nUsage: ldt make <name>",
    "delete": "Delete file/folder\nUsage: ldt delete <name> [--force]",
    "clear": "Clear terminal\nUsage: ldt clear",
    "rename": "Rename file\nUsage: ldt rename <old_name> <new_name>",
    "rename-folder": "Rename folder\nUsage: ldt rename-folder <old_folder> <new_folder>",
    "head": "Show first n lines of file\nUsage: ldt head <file> [lines]",
    "tail": "Show last n lines of file\nUsage: ldt tail <file> [lines]",
}

def show_help(args):
    if len(args) < 3:
        print("Available commands:")
        for cmd in help_data:
            print(" -", cmd)
        return

    cmd = args[2]

    if cmd in help_data:
        print(help_data[cmd])
    else:
        print("Command not found")