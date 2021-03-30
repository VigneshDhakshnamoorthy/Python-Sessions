with open("Files/file_read_write_append.txt",'r') as file:
    print(file.read(10),end="")
    print(file.read(10))