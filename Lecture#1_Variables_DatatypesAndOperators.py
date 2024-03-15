# Print Function
print("hello world")
print("how are you")
print("Apna College")

print("owsom", "toturial")

print (33+99)
print(44/3)

# Variables
name = "irfan"
age = 22
price = 22.3

print(age , "its a integer number") # valid

print(name + "its a integer number") #valid

# print(price + "its a integer number")#not valid


print(type(age))
print(type(name))
print(type(price))

old = None

print(type(old))

# Comments
# single line comment
"""multi 
line 
comment"""

#Arithmatic operators(+ - * / % **)
a = 5
b = 2
print("a = ", a , "& b = ", b)
print("a + b = ", a+b)
print("a + b = ", a-b)
print("a * b = ", a*b)
print("a / b = ", a/b)
print("a % b = ", a%b)
print("a ** b = ", a ** b)


# # unary operators(incremet and decremetn with post and pre)
# a = a + 1
# print(a)#6

# #print(a++)# the print value of a is 5 becuase its a post increment 
# a = a - 1
# print(a)#4

# a = ++a
# print(a)# the print value of a is 6 becuase its a pre increment

# #a = a--
# print(a)# the print value of a is 5 becuase its a post degrement

# a = --a
# print(a)# the print value of a is 4 becuase its a pre degrement

# a = a * 1
# print(a)# 5

# a = a / 5
# print(a)# 1

# a = a % 2
# print(a)#


# Assingment Operators(= += -= *= %= **=)
a += 1# a = a + 1; its a same one
print(a)

a -= 1# a = a - 1; its a same one
print(a) 

a *= 1# a = a * 1; its a same one
print(a) 

a /= 1# a = a / 1; its a same one
print(a)

a %= 1# a = a % 1; its a same one
print(a); 

a **= 1# a = a ** 1; its a same one
print(a); 


# comparison Operators

# 1. equal to (==)
# 2. not equal to (!=)
# 5. greater than >
# 6. less than <
# 7. greater than and equal to >=
# 8. less than and equal to <=


x = 5
y = 2
print("5 == 2", x == y)# output false
y = 5
print("5 == 5", x == y)# output true
print("5 != 5", not (x == y))# output false

z = "5"# string
print("5 == 5", x == z)# output false different from injavaScript(true)
print("5 == 5", x == z)# output false
# print("5 === 5", x === z)# output true
# print("5 !== 5", x !== z)# output false
y = 2
print("5 > 2", x > y)# output true
print("2 < 5", y < x)# output true
print("2 <= 5", y <= x)# output true
print("5 >= 2", x >= y)# output true


# Logical Operators
print("2 < 5 , 5 > 2", y < x and x > y)# both condition should be true
print("2 > 5 , 5 > 2", y > x or x > y)# one condition should be true
print("2 < 5",  not(y > x))# this operator give me a opposite answer which is fase


# Type Conversion
# this type of convertion automatically exist in python language
a = 5
b = 5.5
sum = a + b
print(a+b)# the answer is in float which is by default

# Typecasting
# this type of convertion occure with hard code means externally when we need
a = 2
b = int("4")
print(type(b))

sub = a - b
print(sub)

x = "hello"
y = str(2)

print(type(y))

print(x+y)


# Inputs in Python

name = input("Enter name : ") # its a by default Str
age = int(input("Enter your age : ")) # TypeCasting
marks = float(input("Enter your marks : ")) # TypeCasting

print(type(name), name)
print(type(age), age)
print(type(marks), marks)

# Lets Practise some questions
# Write a porgrame to input two numbers and print their sum.
x = float(input("first number: "))
y = float(input("second number: "))

print("Sume = ", x + y)



# WAP to input side of a square & print its area.
side = float(input("Enter side of square: "))
print("Area of this square is: ", side * side)
print("Area of this square is: ", side ** 2)

# WAP input two floating point numbers & print thier average.
num1 = float(input("first number: "))
num2 = float(input("second number: "))

average = (num1 + num2) / 2
print("Average is: ", average)

# WAP to input two integers number, a and b.
# print True if a is greater than or equal to b. If not print False.

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))

print(a>=b)

if a>=b:
    print("True")
else:
    print("False")









