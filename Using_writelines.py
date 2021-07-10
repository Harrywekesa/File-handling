with open('writelines_file.txt', 'w') as output_file:
    lines_to_write = "Hello! \nMy name is Harrison wekesa wanjala \nI am an African, to be specific, I am Kenyan.\nI was born in 1998, mid octobers in a town called Thika."
    output_file.writelines(lines_to_write)