#!/usr/bin/python

aCoolList = ["superman", "spiderman", 1947,1987,"Spiderman"]

oneMoreList = [22, 34, 56,34, 34, 78, 98]

# extending the list

# Before:
print (aCoolList)
print(type(aCoolList),len(aCoolList))

aCoolList.extend(oneMoreList)
# After:

print (aCoolList)
print(type(aCoolList),len(aCoolList))

"""
Extend the list by appending all the items in the given list;
equivalent to a[len(a):] = L.
"""
