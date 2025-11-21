#star pyramid left side pattern
# n=int(input("Enter number of rows: "))
# for i in range(1,n+1):
#     print("* "* i)
#     i+=1

#star pyramid right side pattern
# m=int(input("Enter number of rows: "))
# for i in range(1,m+1):
#     print(" "*(m-i),end=" ")   #end prevents to goto next line immideatly
#     print("*"*i)


# middle pyramid
rows=int(input("enter the number: "))
for i in range(1, rows + 1):
    # Print leading spaces
    print(' ' * (rows - i-1), end='')
    # Print stars with spaces
    print('* ' * i)

#reverse pyramid left side pattern
def reverse_pyramid(n):
    for i in range(n,0,-1):
        print("* "* i)
        i-=1
print(reverse_pyramid(5))

#inches into cm
def inches_to_cm(inches):
    return inches * 2.54
print(inches_to_cm(5))

#multiplication table
def multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
multiplication_table(5) 