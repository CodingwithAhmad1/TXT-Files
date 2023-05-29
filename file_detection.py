import os
path = "C:\Windows\System32\cmd.exe"

if os.path.exists(path):
    print("Path exists")
    if os.path.isfile(path): # if its a file
        print("That is a file")
        
    elif os.path.isdir(path): # if its a path
        print("It's a directory")
else:
    print("Path doesn't exist")