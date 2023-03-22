# Read Mode
"""
file = open("File_IO_Basics", "rb")
contents = file.read(89)
print(contents)
print(file.readline())
print(file.readline())
# print(file.readline())
print(file.readlines())
"""
# Write Mode
'''
f = open("File_IO_Basics", "w")
a = f.write("Wonder Woman bhi acchi hai")
print(a)
f.close()
'''
# Append  Mode
'''
f = open("File_IO_Basics", "a")
f.write("Wonder Woman bhi acchi hai")
'''
# Read and Write Mode
f = open("File_IO_Basics", "r+")
print(f.read())
f.write("\nblack widow flop hai")
print(f.read())
