
try: # if file exists
    with open('test.txt') as file: #if its a directory, write within brackets
        print(file.read())
        
except FileNotFoundError: # if there is an error
    print("File not found")