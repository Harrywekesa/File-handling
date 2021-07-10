with open('writelines_file.txt','a') as output_file:
    lines_to_add = "\nHabari gani ? \nKwa majina najulikana kama Bwana Wekesa wanjala Harrison,\
        nimezaliawa mwaka wa 1998 \nMjini Thika.Mimi ni mkenya."
    output_file.writelines(lines_to_add)