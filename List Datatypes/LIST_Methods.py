#!/usr/bin/python

aCoolList = ["superman", "spiderman", 1947,1947]
oneMoreList = [22, 34, 56,34, 34, 78, 98]

# using these methods is much more common

print (aCoolList.count(1947))
print (oneMoreList.count(34))

# extending the list
aCoolList.extend(oneMoreList)
print (aCoolList)

# finding index

print (oneMoreList.index(98))

# inserting values
aCoolList.insert(0, "street750")
print (aCoolList)

# deleting values

aCoolList.pop(2)
print (aCoolList)
aCoolList.remove(1947)
print (aCoolList)

# sorting and reversing
print (oneMoreList)
oneMoreList.reverse()
print (oneMoreList)

oneMoreList.sort()
print (oneMoreList)
