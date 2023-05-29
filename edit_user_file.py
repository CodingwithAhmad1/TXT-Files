import shutil
import os
# path = "C:\Windows\System32\cmd.exe"
# path1 = input("Enter file path: ")

# while True:
#     if os.path.isfile(path): # if its a file
#         print("That is a file")
#         shutil.copyfile('text.txt', 'copy.txt')
#         break
#     else:
#         path1 = input("Enter valid path: ")



# Python program to replace text in a file


with open('test.txt') as f:
    content = f.read()

shutil.copyfile('test.txt', 'copy.txt') 
f = open("copy.txt", "r+")

f.truncate(0) # removes all content
f.write(content) # writes new content
f.close()
print("Text successfully replaced")
            
    