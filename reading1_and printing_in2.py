with open('output_file.txt', 'r') as input_file, open('writelines_file.txt', 'a') as output_file:
    for line in input_file.readlines():
        output_file.writelines(line)