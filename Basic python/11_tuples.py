'''
Python Tuple is a collection of objects separated by commas. In some ways, a tuple is similar to a list in terms of indexing, nested objects, and repetition
but a tuple is immutable, unlike lists which are mutable. A tuple is a collection which is ordered and unchangeable(Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

).Tuples are written with round brackets.


'''


# s = "Anuj"
# s[0] = 'C'

a = ('A', 'n', 'u', 'j')
a[0] = 'c' #not supported


print(a)


#ex-2
var = ("Geeks", "for", "Geeks")

print("Value in Var[0] = ", var[0])
print("Value in Var[1] = ", var[1])
print("Value in Var[2] = ", var[2])


#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

thistuple = ("apple",)
print(type(thistuple))


#It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#---------------------------------Access-------------------------------------


#Access of tuple elements is same as list

#-----------------------------------------update-------------------------------------------
#update
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.But there is a workaround for add, change ,remove.
#You can convert the tuple into a list, change the list, and convert the list back into a tuple

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many),
#create a new tuple with the item(s), and add it to the existing tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
print(x)

#The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists


#--------------------------------------------------unpack tuple------------------------------------------------------------------

#unpack tuple --When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

fruits = ("apple", "banana", "cherry")

#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#--------------------------------------------looping----------------------------------------------

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  
  #Use the range() and len() functions to create a suitable iterable.

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
  
  #while
  thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
  
  
  #-------------------------------------------------------join tuples------------------------------------------------
  
  #To join two or more tuples you can use the + operator:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#If you want to multiply the content of a tuple a given number of times, you can use the * operator:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#---------------------------------------------method---------------------------------

'''Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found'''




































