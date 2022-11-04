#Sets are used to store multiple items in a single variable.A set is a collection which is unordered(Note: Sets are unordered, 
#so you cannot be sure in which order the items will appear.), unchangeable*, and unindexed.Sets are written with curly brackets.
#* Note: Set items are unchangeable, but you can remove items and add new items.
#Set items are unordered, unchangeable, and do not allow duplicate values.



thisset = {"apple", "banana", "cherry"}
print(thisset)

#It is also possible to use the set() constructor to make a set.



thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#--------------------------Access is same--------------------------------

#---------------------Update-------------------------------------------

#Once a set is created, you cannot change its items, but you can add new items.

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


#add sets--To add items from another set or any iterable into the current set, use the update() method.

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#remove
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#Note: If the item to remove does not exist, remove() will raise an error.

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#Note: If the item to remove does not exist, discard() will NOT raise an error.

#Remove the last item by using the pop() method:

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
#Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

#The clear() method empties the set:

#The del keyword will delete the set completely:

#----------------------looping same-----------------------------------------------------------
#------------------------------join sets-------------------------------------------------

#The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#Note: Both union() and update() will exclude any duplicate items.

#The intersection_update() method will keep only the items that are present in both sets.

#The intersection() method will return a new set, that only contains the items that are present in both sets.

#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

#The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.







#----------------------------------------------------------methods------------------------------

'''Method	Description
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others'''






















