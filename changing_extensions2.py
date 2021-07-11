import glob #Helps match patterns in file names
import os

path = "/home/harrison/Documents/notes/Practical files/File handling/modified/"
possible_file_names = os.path.join(path, "*.jpg")
for file in glob.glob(possible_file_names):
    print("Converting... {} to png".format(file))
    fullname = os.path.join(path,file)
    newfile = fullname[0:len(fullname)-4] + ".png"
    os.rename(fullname, newfile)