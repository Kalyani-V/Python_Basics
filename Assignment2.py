#Python using Informatics
#Assignment 2- Functions
#Kalyani Vaidya

print("String conversion to integer")
def to_number(str):
    return(int(str))

str=input("Enter a string:")
to_number(str)


print("Addition of two numbers")
def add_two(n1,n2):
    return(n1+n2)
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print("Sum of two numbers: {} , {} is : {}".format(a,b,add_two(a,b)))

print("Cube of a number")
def cube(n):
    return(n * n * n)
c=int(input("Enter any number: "))
print("Cube of a number {} is : {}".format(c,cube(c)))

s1=input("Enter first string :")
s2=input("Enter second string :")
print("After string to integer conversion")
c1=add_two(to_number(s1),to_number(s2))
print("Sum of two numbers is : ",format(c1))
print("Cube of a number {} is : {}".format(c1,cube(c1)))
print("Only one statement: Answer is: {} ".format(cube(add_two(to_number(s1),to_number(s2)))))
