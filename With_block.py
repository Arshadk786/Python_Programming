q = open("File_IO_Basics", "rb")
print(q.readlines())
print(q.read())


with open("File_IO_Basics", "rb") as f:
    print(f.readlines())
    print(f.read())
    
