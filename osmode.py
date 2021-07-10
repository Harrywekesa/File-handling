import os

path = "/home/harrison/Documents/notes/Practical files/File handling/"
input_file_name = os.path.join(path, 'write_lines.txt')
with open(input_file_name, 'r') as file:
    for line in file.readlines():
        print(line)