
/* 
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

*/

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])


print(thisdict)

#Dictionaries cannot have two items with the same key:Duplicate values will overwrite existing values:

#------------------------------------------------Access---------------------------------------

#You can access the items of a dictionary by referring to its key name, inside square brackets:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

#There is also a method called get() that will give you the same result:

x = thisdict.get("model")
#The keys() method will return a list of all the keys in the dictionary.

x = thisdict.keys()

#The values() method will return a list of all the values in the dictionary.
x = thisdict.values()

#The items() method will return each item in a dictionary, as tuples in a list.

x = thisdict.items()

#--------------------------------update----------------------------------------------
#You can change the value of a specific item by referring to its key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#Adding an item to the dictionary is done by using a new index key and assigning a value to it:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#There are several methods to remove items from a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


#The popitem() method removes the last inserted item 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
#The del keyword removes the item with the specified key name:

#The clear() method empties the dictionary:

#Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#Another way to make a copy is to use the built-in function dict().
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#---------------------------------------------looping-------------------------------------

#Print all key names in the dictionary, one by one:
for x in thisdict:
  print(x)
  
  #Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])
  
  #You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
  print(x)
  
  #You can use the keys() method to return the keys of a dictionary:
  for x in thisdict.keys():
  print(x)
  
  #Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
  print(x, y)
  
  
  #--------------------------------------------nested dict---------------------------------
#Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#Or, if you want to add three dictionaries into a new dictionary:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}






