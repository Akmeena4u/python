#Strings in python are surrounded by either single quotation marks, or double quotation marks.
#You can assign a multiline string to a variable by using three quotes it may be double or single:

a = "Hello"
print(a)  //single line string


a = """Lorem ipsum dolor sit amet,    #multiline string
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello, World!"
print(a[1])   # accessing string element --string as array


for x in "banana":
  print(x)    #looping in string
  
  #-----------------------------------------------------------------------------------------------------------------------
  
  
  #string functions
  #length--The len() function returns the length of a string:

a = "Hello, World!"
print(len(a))

#check--To check if a certain phrase or character is present in a string, we can use the keyword in.

txt = "The best things in life are free!"
print("free" in txt)

#check if not --To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "The best things in life are free!"
print("expensive" not in txt)

#slicing--You can return a range of characters by using the slice syntax.
b = "Hello, World!"
print(b[2:5])
print(b[:5])  #slice from the start
print(b[2:])  #slice from end


#negative index--Use negative indexes to start the slice from the end of the string:
print(b[-5:-2])


#--------------------------------------------------------------------------------------------------------------


#Python has a set of built-in methods that you can use on strings.

#modify--

a = "Hello, World!"
print(a.upper())
print(a.lower())
print(a.strip()) # returns "Hello, World!"
print(a.replace("H", "J"))
print(a.split(",")) # returns ['Hello', ' World!']   The split() method splits the string into substrings if it finds instances of the separator:



#------------------------------------------------------------------------------------------------------------------

#concatenation--To concatenate, or combine, two strings you can use the + operator.

a = "Hello"
b = "World"
c = a + b
print(c)

#To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)


#-----------------------------------------------------------------------------------------------------------------------
#format string ---The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:

'''age = 36
txt = "My name is John, I am " + age   #error
print(txt)'''

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


#----------------------------------------------------------------------------------------------------------------------------------
#escape seq--To insert characters that are illegal in a string, use an escape character.An escape character is a backslash \ followed by the character you want to insert

txt = "We are the so-called \"Vikings\" from the north."



#------------------------------------------------------------------------------------------------------------------------------

#string methods
'''
Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning

'''


























# password = "abcdABA$"
# print(password.isalpha())

s = "ABCDE$%"
# print('s.isalpha', s.isalpha())
# print('s.isdigit', s.isdigit())
# print('s.islower', s.islower())
# print('s.isupper', s.isupper())


# print('s.lower', s.lower())
# print('s.upper', s.upper())

x = '    abc     '
print(x.lstrip())






















# a = "abc"

# for my_char in a:
# 	print(my_char*2)























# b = 'def'

# # c = a+b

# c = a*3

# print(c)























# fruit = "Apple"

# # print(fruit[4])

# print(fruit[-2])

# my_char = fruit[2];
# print(my_char)





# name = """Anuj
# Kumar 
# Sharma"""
# paragraph = ''' This is a 
# multiline
# String
# paragraph. This is for testing'''

# print(name)
