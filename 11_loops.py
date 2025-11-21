for i in range(1,6): #range(start, stop, step)
    print(i)
    
i=1
while i<=5:
    print(i)
    i+=1

#for else statement (rarely used)
n=int(input("Enter a number: "))
for i in range(1,11):
    print("",n,"*",i,"=",i*n)
else:
    print("Multiplication table of",n,"is printed successfully")
    
#while else statement (rarely used)
count=1
while count<=10:
    print("Count is:",count)
    count+=1
else:
    print("Counting completed successfully")
    
#nested loops
for i in range(1,4):  #outer loop
    for j in range(1,4):  #inner loop
        print("i =",i,"j =",j)

#break statement
for i in range(1,11):
    if i==6:
        break
    print(i)