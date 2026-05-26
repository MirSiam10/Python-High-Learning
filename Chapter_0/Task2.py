import os

# Specify the directory path
path = "/"

# Get and print all files and folders
contents = os.listdir(path)

for item in contents:
    print(item)