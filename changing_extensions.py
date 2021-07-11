import os

path = "/home/harrison/Documents/notes/Practical files/File handling/modified/"

#getting a list of all files and folders
all_files = os.listdir(path)

#Loop over every file in the list
for file in all_files:
    if file.lower().endswith(".png"): #extension ends with png
        print("Converting...{} to jpg".format(file))
        #get file name and change it from .png to .jpg 
        fullname = os.path.join(path, file)
        newname = fullname[0:len(fullname)-4] + ".jpg"
        os.rename(fullname, newname)
        