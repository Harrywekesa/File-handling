import os

path = "/home/harrison/Documents/"

for currentFolder, subfolders, files in os.walk(path): #Walk returns all possible combinations of folders subfolders and files in a directory
    for filename in files:
        print(os.path.join(currentFolder, filename))