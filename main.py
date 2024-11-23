import os
import re

def user_input():
     print("Input the command")
     command = input("> ")
     print(f"> {command}")
     return command

def print_currdir():
     current = os.getcwd()
     print(current)

def change_dir():
     current = os.chdir("../")
     path = os.getcwd().split("\\")[-1]
     print(path)

def print_fileList():
    fileList = os.listdir()
    print(fileList)
    return fileList

def print_fileListWithSize(fileList):
    for file in fileList:
        if os.path.isfile(file) == True:
            filewithSize = os.stat(file).st_size
            print(f"{file} {filewithSize}")
        else:
            print(file)

def print_fileSizeinH(fileList):
    for file in fileList:
        if os.path.isfile(file) == True:
            filewithSize = os.stat(file).st_size
            if filewithSize < 1024:
                print(f"{file} {filewithSize}B")
            elif filewithSize >= 1024 and filewithSize < (1024 * 1024):
                filewithSize = round(filewithSize / 1024)
                print(f"{file} {filewithSize}KB")
            elif filewithSize >= (1024 * 1024) and filewithSize < (1024 * 1024 * 1024):
                filewithSize = round(filewithSize / (1024 * 1024))
                print(f"{file} {filewithSize}MB")
            elif filewithSize >= (1024 * 1024 * 1024) and filewithSize < (1024 * 1024 * 1024 * 1024):
                filewithSize = round(filewithSize / (1024 * 1024 * 1024))
                print(f"{file} {filewithSize}GB")
        else:
            print(file)

def make_newFile(command):
    try:
        cm, path = command.split(" ")[0], command.split(" ")[1]
        current = os.getcwd()
        try:
            os.mkdir(f"{current}/{path}")
        except:
            print("The directory already exists")
    except:
        print("Specify the name of the directory to be made")

def remove_fileDirectory(command):
    try:
        os.path.isdir("command.split(" ")[1]")
        try:
            cm, path = command.split(" ")[0], command.split(" ")[1] # make them friendly to reader, more readability!
            current = os.getcwd() # overused of os.getcwd() could do it as constant or global variable
            try:
                os.rmdir(f"{current}/{path}")
            except:
                print("No such file or directory")
        except:
            print("Specify the file or directory")
    except:
        try:
            cm, path = command.split(" ")[0], command.split(" ")[1]
            current = os.getcwd()
            try:
                os.remove(f"{current}/{path}")
            except:
                print("No such file or directory")
        except:
            print("Specify the file or directory")

def rename_fileDirectory(command):
    try:
        cm, old, new = command.split(" ")[0], command.split(" ")[1], command.split(" ")[2]
        if not os.path.exists(old):
            print("No such file or directory")
        if os.path.exists(new):
            print("The file or directory already exists")
        os.rename(old, new)
    except:
        print("Specify the current name of the file or directory and the new name") # error handling bug


while(user_input() != "quit"):
      command = user_input()
      if command == "pwd":
        print_currdir()
      elif command == "cd ..":
        change_dir()
      elif command == "ls":
        fileList = print_fileList()
      elif command == "ls -l":
        print_fileListWithSize(fileList)
      elif command == "ls -lh":
        print_fileSizeinH(fileList)
      elif re.match("^mkdir", command):
        make_newFile(command)
      elif re.match("^rm", command):
        remove_fileDirectory(command)
      elif re.match("^mv", command):
        rename_fileDirectory(command)
      else:
        print("Invalid Command")
