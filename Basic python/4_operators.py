

#logical

x = True
y = True

print('x and y is',x and y)

print('x or y is',x or y)

print('not x is',not x)


#----------------------------------------------------------------------------------------------------------------------------------------


#Comparison Operators



 a = 45
 b = 45

 print('a > b', a > b)
 print('a < b', a < b)
 print('a >= b', a >= b)
 print('a <= b', a <= b)
 print('a == b', a == b)
 print('a != b', a != b)



 a =  6
 a = a + 5
 a += 5
 a -= 5
 a *= 5
 a /= 5

 print(a)



 first_number = 4
 second_number = 7
 third_number = 8

 average = (first_number +
  second_number + 
  third_number) / 3

 print(average)

 a = 5
 b = 3

# # This line is for adding
 c = a+b
 print(c)

#------------------------------------------------------------------------------------------------------------------------------------------
# '''Arithmetic Operators
print(a+b)
 print(a-b)
 print(a*b) print(a/b)

print(a%b)
 print(a//b)
 print(a**b)
# '''

#The bool() function allows you to evaluate any value, and give you True or False in return,
#Almost any value is evaluated to True if it has some sort of content.

#-------------------------------------------------------------------------------------------------------------------------------------------

#Identity Operators--Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

#--------------------------------------------------------------------------------------------------------------------------------

#Membership operators are used to test if a sequence is presented in an object
x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list

