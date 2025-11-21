a=int(input("Enter value for a: "))
b=int(input("Enter value for b: "))

# If else statement
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")

# If elif else statement
if a>b:
    print("a is greater than b")
elif a==b:
    print("a is equal to b")
else:
    print("b is greater than a")

# Nested if statement
if a>b:
    if a>b+1:
        print("a is greater than b+1")
    else:
        print("a is not greater than b+1")
else:
    print("b is greater than a")

# Conditional Operator (something new)
print("a is greater than b" if a>b else "b is greater than a")

