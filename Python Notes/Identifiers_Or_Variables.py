#!/usr/bin/python

#! = Shebang
# /usr/bin/python = Absolute path of the python

# Creating variables in python

# A-Z     # Hash means single line comment
# a-z
# combinations of A-Z & a-z
# 0-9
# combinations of A-Z , a-z & 0-9
# an underscore (_).
# combinations of A-Z , a-z , 0-9 & _

# Below is the multi-line comment """ """ or ''' ''''
"""We can use camel-case style i.e.,
capitalize every first letter of the word
except the initial word without any spaces."""

'''This is
multi-line
comment'''

highScoreValue = 1          # Camel-Case Style Variable
a = 1
A = 2

#007Redhat = 100   # We are not suppose to use 0-9 as variable names as prefix.
Red_007_hat = 100   
_007= 200
_007_PyCharm = 200

tools="pycharm"
ide_tools='anacodna'

course="""Python
Python Basic and Advanced
Python CGI
"""

version='''Python 2.x
Python 3.x
Pycharm - Is a IDE tool
Spyder - Is a IDE tool
'''

# Let's access variables

print("Lets access Camel-Case Style Variable : ",highScoreValue,type(highScoreValue),id(highScoreValue))
print("")
print(a,"Access a lower case variable",type(a),id(a))
print("")
print("Access a upper case ",A,"variable",type(A),id(A))
print("")
print("Lets use combination of all : ",Red_007_hat,type(Red_007_hat),id(Red_007_hat))
print("")
print(_007,type(_007),id(_007))
print("")
print("UnderScore Digits and Alphabets: ",_007_PyCharm,type(_007_PyCharm),id(_007_PyCharm))
print(tools,type(tools),id(tools))
print(ide_tools,type(ide_tools),id(ide_tools))
print("")
print("We are calling course",course,type(course),id(course))
print("")
print("Calling version",version,type(version),id(version))
