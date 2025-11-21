#making copy of file

# with open("ex/word.txt","r") as f:
#     content = f.read()
    
# with open("ex/word_copy.txt","w") as f:
#     content = f.write(content)
    
#matching content in file

with open("ex/word.txt","r") as f:
    content1 = f.read()
    
with open("ex/word_copy.txt","r") as f:
    content2 = f.read()

if content1 == content2:
    print("Both files are same")
else:
    print("Files are different")
    
#rename the file

import os
os.rename("ex/word_copy.txt","ex/word_renamed.txt")
