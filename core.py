import os
import shutil
from pathlib import Path


class FileManager:
    def __init__(self, work_dir):
        self.WORK_DIR = Path(work_dir).absolute()
        try:
            os.chdir(self.WORK_DIR)
        except FileNotFoundError:
            print("File not found exception")
        self.curr_dir = Path(work_dir).absolute()
        self.last_dir = self.WORK_DIR.name


    def helper(self):

        print("make_dir {name}               create directory {name}")
        print("del_dir {name}                delete directory {name}")
        print("ch_dir {name}                 change work directory")
        print("make_file {name}              create empty file {name}")
        print("write_file {name} {data}      write {data} to file {name}")
        print("read_file  {name}             Viewing the contents of a text file")
        print("del_file  {name}              delete file {name}")
        print("copy_file {name} {new_dir}    copy file from {name} to {new_dir}")
        print("move_file {dir} {new_dir}     move file from {name} to {new_name}")
        print("rename_file {name} {new_name} rename file from {name} to {new_name}")
        print("tree_list                     Show file structure")
        print("curr                          Show work dir")
        print("help or ?                     Manual")
        print("quit or q                     Exit from program")


    def get_curr_dir(self):
        return os.getcwd()

    def tree_list(self):
        if os.listdir(path=self.curr_dir):
            for item in os.listdir(path=self.curr_dir):
                print(item)
        else:
            print("Folder is empty")

    def make_dir(self, path):
        try:
            if os.path.exists(path):
                print("Folder with the same name is exist")
            else:
                os.makedirs(str(path))
                print(f'Folder {path.split("/")[-1]} is create successfully')
        except FileNotFoundError:
            print("Incorrect path")

    def del_dir(self, path):
        if os.path.isdir(path):
            shutil.rmtree(str(path), ignore_errors=True)
            print("Folder", path.split("/")[-1], "delete.")
        else:
            print("Directory with this name is not found")

    def ch_dir(self, path):
        try:
            if len(path) != 0:
                if path == "..":
                    if self.last_dir in str(self.curr_dir.parent):
                        os.chdir(self.curr_dir.parent)
                        self.curr_dir = self.WORK_DIR.joinpath(self.curr_dir.parent)
                        print("Current path:", self.curr_dir)
                    else:
                        print("Unable to go outside the working folder!")
                else:
                    os.chdir(path)
                    self.curr_dir = self.WORK_DIR.joinpath(path)
                    print("Current path:", self.curr_dir)
        except FileNotFoundError:
            print("There is no folder with this name.")
        except OSError:
            print("There is no folder with this name.")

    def make_file(self, path):

        try:
            if os.path.exists(path):
                print("A file with the same name already exists")
            else:
                open(path, "w", encoding="utf-8").close()
                print('File is created')
        except FileNotFoundError:
            print("File path not found")


    def write_file(self, path, inner):
        try:
            self.curr_dir.joinpath(path).write_text(inner)
            print(f"Data '{inner}' is writed in {path}.")
        except FileNotFoundError:
            print("File not found")

    def read_file(self, path):
        try:
            if os.path.exists(path):
                print(str(self.curr_dir.joinpath(path).read_text()))
            else:
                print("File with this name does not exist")
        except OSError:
            print("File with this name does not exist")

    def del_file(self, path):
        try:
            if os.path.exists(path):
                os.remove(self.curr_dir.joinpath(path))
                print(f"File {path} is deleted.")
            else:
                print("File with this name does not exist")
        except OSError:
            print("File with this name does not exist")

    def copy_file(self, curr_path, new_path):
        try:
            if os.path.exists(curr_path):
                shutil.copy2(curr_path, new_path)
                print(f"File is copied in {new_path}")
            else:
                print("File with this name does not exist")
        except OSError:
            print("File with this name does not exist")

    def move_file(self, curr_path, new_path):
        try:
            if os.path.exists(curr_path):
                os.replace(curr_path, new_path)
                print(f"File id moved from {curr_path} in {new_path}")
            else:
                print("File with this name does not exist")
        except OSError:
            print("File with this name does not exist")

    def rename_file(self, path, new_name):
        try:
            if os.path.exists(path):
                self.curr_dir.joinpath(path).rename(new_name)
                print(f"File is renamed {new_name}")
            else:
                print("File with this name does not exist")
        except FileExistsError:
            print("File is already exist")
