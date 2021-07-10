myfile = "/home/harrison/Documents/notes/Practical files/File handling/writelines_file.txt" 
with open(myfile, 'r') as file:
    for line in file:
        print(line)