import os

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

while(user_input() != "quit"):
      command = user_input()
      if command == "pwd":
        print_currdir()
      elif command == "cd ..":
        change_dir()
      elif command == "ls":
        print_fileList()
      else:
        print("Invalid Command")
