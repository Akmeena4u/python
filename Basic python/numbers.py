#There are three numeric types in Python: int , float , complex number
#To verify the type of any object in Python, use the type() function:


x = 1
y = 35656222554887711
z = -3255522
w = 1.0;
t = 35e3
#Float can also be scientific numbers with an "e" to indicate the power of 10
u = 3+5j
    #Complex numbers are written with a "j" as the imaginary part:

       
print(type(x))
print(type(y))
print(type(z))
print(type(w))
print(type(t))
print(type(u))


#You can convert from one type to another with the int(), float(), and complex() methods:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Note: You cannot convert complex numbers into another number type.

#Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

import random

print(random.randrange(1, 10))
