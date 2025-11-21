f=open("00_first.py","r")  #open file in read mode the bydefault mode is read
print(f.read())
f.close()  #close the file

#with statement automatically closes the file after its suite finishes
with open("00_first.py","r") as f:
    content=f.read()
    print(content)

# f=open("00_first.py","w")  #open file in write mode
# f.write("#this is a comment line\nprint('hello world')\n")
# f.close()

f=open("00_first.py","r")  #open file in read mode
line=f.readline()
while(line!=[]):
    print(line)
    line=f.readline()
f.close()  #close the file

#append file
f=open("00_first.py","a")  #open file in append mode
f.write("\n#this line is appended\n")
f.close()

#rb and wb mode are use for reading and writing binary files like images and videos
f=open("15_fileIO.png","rb")  #open image file in read binary mode
data=f.read()
f.close()

