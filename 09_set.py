e=set() #empty set
print(type(e))

#sets are unordered collection of unique elements

s={1,2,3,4,5,1,2,3,"sahil","subham","sahil"}
print(s)  # it will print unique elements only it will remove duplicates

s.add(7)  
print(s)

s.pop()  # removes random element from set
s.remove(3)  # removes specific element from set
s.discard(10)  # it will not give error if element is not present in set
s.clear()  # removes all elements from set
s.union({8,9,10})  # adds elements of both sets

#subsets
s1={1,2,3}
s2={1,2,3,4,5}
print(s1.issubset(s2))
print(s1.issuperset(s2))

word=input("Enter a word: ")
for letter in s1:
    if letter == word:
        print("you found it",letter)
print("good luck next time you fool")

d={}
name= input("Enter your name: ")
lang= input("Enter your language: ")

d.update({name:lang})
name= input("Enter your name: ")
lang= input("Enter your language: ")

d.update({name:lang})
name= input("Enter your name: ")
lang= input("Enter your language: ")

d.update({name:lang})
name= input("Enter your name: ")
lang= input("Enter your language: ")

d.update({name:lang})
print(d)