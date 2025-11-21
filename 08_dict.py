marks= {
    "subham":100,
    "sahil":95,
    "prince":90
}

ag={}  # empty dictionary


print(marks,type(marks))

print(marks.keys())  #it will print the names of students
print(marks.values()) #it will print the marks of students  

marks.update({"ankit":85})  # to add new key value pair in dictionary or can edit existing value
print(marks.get("sahil4"))  # prints none
print(marks["sahil4"]) # return an error

marks.pop("prince")  # it will remove the key value pair of prince
print(marks)

marks.popitem()  # it will remove the last key value pair in dictionary
print(marks)

marks.clear()  # it will remove all key value pairs from dictionary
print(marks)
