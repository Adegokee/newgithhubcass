# thisset = {"apple", "banana", "cherry"}
# print(type(thisset))
# print(thisset)


# thisset = {"apple", "banana", "cherry", "apple"}
# print(type(thisset))
# print(thisset)


# thisset = {"apple", "banana", "cherry", 1, True, 2}
# print(thisset)
# thisset = {"apple", "banana", "cherry", False, True, 0}
# print(thisset)


# thisset = {"apple", "banana", "cherry"}
# print(len(thisset))
# thisset = set(("apple", "banana", "cherry", "apple")) # note the double round-brackets
# print(thisset)



# accessing data in set
# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)



# thisset = {"apple", "banana", "cherry"}
# print("banana" in thisset)
# thisset = {"apple", "banana", "cherry"}
# print("banana" not in thisset)



# adding to set item
# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)




# removing set
# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thisset)


# thisset = {"apple", "banana", "cherry"}
# thisset.discard("banana")
# print(thisset)





# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop()
# print(x)
# print(thisset)




# deleting variable sets

# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)



# joining set
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)


# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1 | set2
# print(set3)


# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
# myset = set1.union(set2, set3, set4)
# print(myset)


# x = {"a", "b", "c"}
# y = (1, 2, 3)

# z = x.union(y)
# print(z)


# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set1.update(set2)
# print(set1)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.intersection(set2)
# print(set3)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 & set2
# print(set3)



# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.intersection_update(set2)

# print(set1)

# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}
# set3 = set1.intersection(set2)
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.difference(set2)

# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 - set2
# print(set3)




# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.difference_update(set2)

# print(set1)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 ^ set2
# print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)