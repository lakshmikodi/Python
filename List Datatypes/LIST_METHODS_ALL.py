#!/usr/bin/python
aCoolList = ["superman",1947, 'spiderman', 1947,1987,"Spiderman"]
oneMoreList = [22, 34, 56,34, 34, 78, 98]

# Trying to find the no.of occurenecs in a variable:
# Method : count(x)

print (aCoolList.count(1947))
print (aCoolList.count('spiderman'))
print (aCoolList.count('spiderman'),aCoolList.count('Spiderman'))
print (oneMoreList.count(34))

# Return the number of times x appears in the list.
# extending the list
# Before:
print (aCoolList)
aCoolList.extend(oneMoreList)
# After:
print (aCoolList)
# finding index
print (oneMoreList.index(56))
print (aCoolList.index(1987))
# inserting values
aCoolList.insert(4, "street750")
print (aCoolList)

# deleting values
aCoolList.pop(4)
print (aCoolList)

print(aCoolList)
aCoolList.remove(1947)
print (aCoolList)

aCoolList.pop()
print (aCoolList)

# sorting and reversing
print (oneMoreList)
oneMoreList.reverse()
print (oneMoreList)

oneMoreList.sort()
print (oneMoreList)

