a= "sahil"
b= " is a good boy"
d=[1,2,3,4,5,6,7,8,9,10]
c= a+b
print(c)
print(a[0])
print(a[-1])
print(len(a))

# slicing 
# a[start:end:jump] if jump is in minus then it will go in reverse order
print(a[0:4:-1]) # it will print from index 0 to end in reverse order
print(a[0:3]) # it will print from index 0 to index 2

print(d[0:10:2]) # it will print from index 0 to index 9 with jump of 2
print(d[9:0:-1]) # it will print from index 9 to index 0 in reverse order with jump of 1
print(d[1:-3]) # it will print from index 0 to end with jump of 3

# some inbuilt functions in strings
print(a.upper()) # it will convert all characters to upper case
print(a.lower()) # it will convert all characters to lower case
print(a.title()) # it will convert first letter of each word to upper case

print(a.capitalize()) # it will convert first letter of string to upper case
print(a.find("i")) # it will return the index of first occurrence of the substring
print(a.rfind("i")) # it will return the index of last occurrence of the substring

print(a.replace("sahil","sahil kumar")) # it will replace the substring with the new substring
print(a.startswith("s")) # it will return True if the string starts with the substring
print(a.endswith("y")) # it will return True if the string ends with the substring

x= "    hello world            "
count= x.count("l")
print("count of l is:",count)
print(x.count(" ")) 


