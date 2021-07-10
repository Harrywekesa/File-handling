with open('writelines_file.txt', 'r') as seekfile:
    print("Line at 0(First line) is :", seekfile.readline()) #readline() prints only one line
    seekfile.seek(0) #JUmping back to the begining
    
    print("Line at 0(First line) is :", seekfile.readline())
    print("Line at position 1 :", seekfile.readline())
    
    seekfile.seek(8)
    print("Line as from position 8: ", seekfile.readline(8))
    
    seekfile.seek(10)
    print("Jumping forward 10 characters. Starting at the 11th character :", seekfile.readline())