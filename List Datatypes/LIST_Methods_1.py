#!/usr/bin/python

ganesh = ['python', 'linux', 1997, 2000]

print ("Value available at index 2 : ")

print (ganesh[2])

ganesh[2] = 1897

print ("New value available at index 2 : ")

print (ganesh[2])

list1 = ['python', 'linux', 1997, 2000];

print (list1)

print (len(list1))

del list1[2];

print ("After deleting value at index 2 : ")

print (list1)

print (len(list1))

list1, list2 = ['abc', 'xyz', 'minnu', 'jessi'], [456, 700, 200]

print ("Max value element : ", max(list1))
print ("Max value element : ", max(list2))


list1, list2 = ['abc', 'xyz', 'minnu', 'jessi'], [456, 700, 200]

print ("Min value element : ", min(list1))
print ("Min value element : ", min(list2))

aTuple = (123, 'xyz', 'minnu', 'jessi')
aList = list(aTuple)

print ("List elements : ", aList)

aList = [123, 'xyz', 'minnu', 'jessi']

aList.append( 2009 );

print ("Updated List : ", aList)

aList = [123, 'xyz', 'minnu', 'jessi', 123];

print ("Count for 123 : ", aList.count(123))
print ("Count for minnu : ", aList.count('minnu'))

aList = [123, 'xyz', 'minnu', 'jessi', 123];

bList = [2009, 'manni'];

aList.extend(bList)

print ("Extended List : ", aList )

aList = [123, 'xyz', 'minnu', 'jessi'];

print ("Index for xyz : ", aList.index( 'jessi' )) 
print ("Index for minnu : ", aList.index( 'minnu' )) 

aList = [123, 'xyz', 'minnu', 'jessi']

aList.insert( 3, 2009)

print ("Final List : ", aList)
aList = [123, 'xyz', 'minnu', 'jessi'];

print ("Before pop method",aList)
print ("A List : ", aList.pop())
print ("Before pop method",aList)
print ("B List : ", aList.pop(2))
print ("After pop method",aList)

aList = [123, 'xyz', 'minnu', 'jessi', 'xyz']

aList.remove('xyz')

print ("List : ", aList)

aList.remove('jessi')

print ("List : ", aList)

aList = [123, 'KKz', 'minnu', 'jessi', 'xyz']

aList.reverse()

print ("List : ", aList)


#aList = ['keshav', 'xyz', 'minnu', 'jessi', 'xyz']
aList = [89,76,44,99,91,10]

aList.sort()

print ("List : ", aList)


