# copyfile() = copy contents of file
# copy() = copyfile() + permission mode + destination can be directory
# copy2() = copy() + copies metadata(file's creation and modifcation times)

import shutil

# you will write directory if not in folder 
shutil.copyfile('test.text', 'copy.txt') # it has been renamed

shutil.copyfile('test.text', 'copy.txt') # you can add a destination and change the name


                                         

