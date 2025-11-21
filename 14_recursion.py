#first n natural numbers using recursion
n= int(input("Enter a positive integer: "))
def natural_numbers(n):
    if n==1:
        return 1
    else:
        return n + natural_numbers(n-1)
print("Sum of first n natural numbers:",natural_numbers(n))  

