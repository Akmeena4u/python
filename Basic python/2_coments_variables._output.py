#Comments starts with a #, and Python will ignore them:
#Python does not really have a syntax for multi line comments.
#Since Python will ignore string literals that are not assigned to a variable,
#you can add a multiline string (triple quotes) in your code, and place your comment inside it:


"""
This is a comment
written in
more than just one line
"""

#The Python print() function is often used to output variables.
#In the print() function, you output multiple variables, separated by a comma

#variables--Variables are containers for storing data values., Variables do not need to be declared with any particular type
#Variable names are case-sensitive.
#String variables can be declared either by using single or double quotes:
x = 5
y = "John"
print(x)
print(y)

# VARIABLE NAMING RULES
#during multiword variable naming u can use camelCase , PasacalCase & snake_case styels
#valid identifiers
age = 24
name = "Amit"
last_name = "kumar"
_id = '23x5342A'
name2 = "Shivam"


#invalid identifiers
2name = "Shivam"
marks$ = 98
class = "Hello"


print(age)
print(name)



#If you want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))


#Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Global variables can be used by everyone, both inside of functions and outside.
#To create a global variable inside a function, you can use the global keyword

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


