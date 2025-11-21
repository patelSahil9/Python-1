friends=["sahil","prince","dev","deep"]
print(friends[0])

# lists are mutable unlike strings or tuples

friends[1]="kumar"
print(friends)
print(friends[1:3])  #slicing


# methods in list
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
l3=l1+l2
print(l3)
print(l1*2)
l1.reverse()
l1.sort()
print(l1)



friends.append("tony")
print(friends)

friends.insert(3,"bruce") # index, value
print(friends)

friends.remove("dev")
print(friends)

friends.pop()
print(friends)