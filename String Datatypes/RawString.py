# Raw strings do not treat the backslash as a special character at all. 

#!/usr/bin/python3
print ('d:\\nowhere')

print ('c:\\nowhere')


# Now let's make use of raw string. 
#We would put expression in r'expression' as follows:

print (r'd:\\nowhere')

print (R'c:\\nowhere')

print (r"d:\\nowhere")

print (R"c:\\nowhere")
