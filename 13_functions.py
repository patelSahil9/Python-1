def avg():                            #defining a function
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))
    average = (a + b + c) / 3
    print("The average is:", average)
    
avg()                             #calling a function

# Builtin functions
# len()
# max()
# min()
# sum()
# abs()

# User defined functions
# like upper code avg() function

def goodday(name,end):               #function with parameter
    print("Have a good day,", name,end=end)
    return                           #return statement so you can use it later in another function
goodday("Alice","!")               #function call with argument
print()                             #just to add a new line
goodday("Bob",".")
    
# greatest of three numbers
def greatest(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
print(greatest(10,20,30))

#celcious to fahrenheit
def c_to_f(c):
    f=(c*9/5)+32
    return f
input_c=float(input("Enter temperature in Celsius: "))
output_f=c_to_f(input_c)
print("Temperature in Fahrenheit:",output_f) 


print("a")
print("b",end="")    #end="" is used to prevent to go to next line
print("c")