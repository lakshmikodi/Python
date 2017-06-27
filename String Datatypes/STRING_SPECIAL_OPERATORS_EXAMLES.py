#!/usr/bin/python
       #01234567891011
       #-11-10-9-8-7-6-5-4-3-2-1
str1 = "Hello World!"  # 11 characters
str2 = 'This is an example string'
        #01234567891011121314151617
"""
print (str1[0])
print (str1[-1])
print (str1[2:6])  # End-1 2:6-1 5 
print (str1[:5])
print (str1 * 3)
print ("updated string ", str1[:6] + "planet")
print ("updated string ", str1[:12] + "Perl")

print(str2[0::2]) # Zero Based indexing
"""

# formatting of strings
print ("Your name is %s and your account id is %d" %("Kevin",14456))

print ("Value1 {} Value2 {} and Value3 {}".format("python",100,"pycharm"))

print ("Calling str1 {0} and calling str2 {1}".format(str1,str2))

print ("Value1 {1} Value2 {0} and Value3 {2}".format("python",100,"pycharm"))

