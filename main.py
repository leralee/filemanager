from core import FileManager
from properties import FM_PATH

fm = FileManager(FM_PATH)
print("Current path: ", fm.get_curr_dir())


while True:
    command = input(">>> ")
    if command.split(' ')[0] == "make_dir":
        new_dir = command.split(' ')[1]
        fm.make_dir(new_dir)

    elif command.split(' ')[0] == "del_dir":
        dirname = command.split(' ')[1]
        fm.del_dir(dirname)

    elif command.split(' ')[0] == "ch_dir":
        dirname = command.split(' ')[1]
        fm.ch_dir(dirname)

    elif command.split(' ')[0] == "make_file":
        filename = command.split(' ')[1]
        fm.make_file(filename)

    elif command.split(' ')[0] == "write_file":
        filename = command.split(' ')[1]
        text = ' '.join(command.split(' ')[2:])
        fm.write_file(filename, text)

    elif command.split(' ')[0] == "read_file":
        filename = command.split(' ')[1]
        fm.read_file(filename)

    elif command.split(' ')[0] == "del_file":
        filename = command.split(' ')[1]
        fm.del_file(filename)

    elif command.split(' ')[0] == "copy_file":
        currpath = command.split(' ')[1]
        newpath = command.split(' ')[2]
        fm.copy_file(currpath, newpath)

    elif command.split(' ')[0] == "move_file":
        currpath = command.split(' ')[1]
        newpath = command.split(' ')[2]
        fm.move_file(currpath, newpath)

    elif command.split(' ')[0] == "rename_file":
        filepath = command.split(' ')[1]
        newname = command.split(' ')[2]
        fm.rename_file(filepath, newname)

    elif command.split(' ')[0] == "curr":
        print("Current path:", fm.get_curr_dir())

    elif command == "tree_list":
        print("Сontents of the current folder: ")
        fm.tree_list()

    elif command == "help":
        fm.helper()

    elif command == "quit":
        print("Exciting from program")
        break
    else:
        print("Wrong command. Use 'help' for manual")