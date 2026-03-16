import sys
f=open("text", "w")
print(f.fileno())

f2=open("test.csv","r")
print(f2.fileno())
f3=open("file.py", "r")

f.write("This is first line\n")

#flush the buffer
f.flush()

f.write("The second line")

print(sys.stdin.isatty())
print(f3.isatty())
f.close()
#read the file complete
f=open("text", "r")
print("readable: ",f.readable())
print(f.read())

#read one line
f=open("text", "r")
print(f.readline())

#read multiple line
f=open("text", "r")
print(f.readlines(20))

f=open("text", "r")
print(f.seekable())
f.seek(7)
print(f.readline())

f2=open("test.csv","r")
f2.seek(2)
print(f2.readline())

f2=open("test.csv","r")
print(f2.tell())