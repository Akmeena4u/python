'''Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members'''


#Lists are used to store multiple items in a single variable.
#List items are ordered( it means that the items have a defined order, and that order will not change.), changeable, and allow duplicate values.
#If you add new items to a list, the new items will be placed at the end of the list.


 a = [6, 2, 3, 9, 1, 6, 4, 5]

 print(len(a))
print(max(a))
print(min(a))
print(type(a))


 print(sum(a))

 for element in a:
   	print(element * 2, end = " ")

    #--------------------------------------------------------------------------------------------------------------
    #list accessing

#It is also possible to use the list() constructor when creating a new list
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
  
  
  #-----------------------------------------------------------------------------------------------------------
  #change in list
  
  thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]    #Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
print(thislist)


#If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

thislist = ["apple", "banana", "cherry"]

thislist[1:3] = ["watermelon"]

print(thislist)




#-------------------------------------------------------------------------------------------------------------------------------------
#Add & remove list items

#To add an item to the end of the list, use the append() method:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#To insert a new list item, without replacing any of the existing values, we can use the insert() method.
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#To append elements from another list to the current list, use the extend() method.

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


#The remove() method removes the specified item.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)                #If you do not specify the index, the pop() method removes the last item



#The del keyword also removes the specified index:
#The del keyword can also delete the list completely.

#The clear() method empties the list.The list still remains, but it has no content.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


#---------------------------------------------------------------------------------------------------------

#looping in list

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
  #List Comprehension offers the shortest syntax for looping through lists:

  thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
  
  
  #------------------------------------------------------------------------------------------------------
  
  #sort list
  
  #List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
  
  thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


#To sort descending, use the keyword argument reverse = True:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#The reverse() method reverses the current sorting order of the elements.

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)



#------------------------------------------------------------------------------------------------
#copy

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


#Another way to make a copy is to use the built-in method list().

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)







# a = [6, 2, 3, 9, 1, 6, 4, 5]
# fruits = ['Banana', 'Apple', 'Kiwi', 'Kiwi']

# a.pop(0)
# print(a)

# a.clear()
# print(a)

# fruits.reverse()
# print(fruits)

# print(fruits.index('Apple'))

# print(fruits.count('Kiwi'))












# # a.sort()
# fruits.sort()

# print(fruits)



















# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# a = [x for x in range(100) if x%2 == 1]
# print(a)

# b = [3**i for i in range(10)]
# print(b)
























# name = 'Anuj'
# name = 234

# fruits = ["Apple",'Guava','Papaya']
# fruits[1] = 'Mango'

# # del fruits

# # print(fruits[-1])

# print(fruits)
