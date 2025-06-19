# Files and Directories

# module: pathlib - Object-oriented filesystem paths

from pathlib import Path

# Referring with an absolute or relative path

Path() #No param will point to the current directory

path = Path("Utility")
print(path.exists()) #to see the path is valid and exist

#creating a folder
path_email = Path("email")
# path_email.mkdir() # to create a directory
# path_email.rmdir()

#To get all files and folder in a directory
path = Path()
print(path.glob('*.*'))
for file in path.glob('*'):
    print(file)