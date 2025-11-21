a=(1,2,3,4,5,"sahil","prince")
print(type(a))  

#we cant change tuple items as they are immutable
# a[1]="kumar"  # this will give error

x=input("enter your fruits separated by comma:")
fruits= tuple(x.split(","))
print(fruits)

marks=[]
m1=int(input("enter marks of subject 1:"))
marks.append(m1)
m2=int(input("enter marks of subject 2:"))
marks.append(m2)
m3=int(input("enter marks of subject 3:"))  
marks.append(m3)
m4=int(input("enter marks of subject 4:"))
marks.append(m4)
m5=int(input("enter marks of subject 5:"))
marks.append(m5)
marks.sort()
print(marks)