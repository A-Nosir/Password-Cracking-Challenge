'''
Name: Justin Tareq 

Class: COMP 3109 

Source: My teammate Saul Hughes is the author of this code 

Purpose of Program: The source code is to generate string
passwords with ascii digits, lowercase letters, and
uppercase letters at length eight. The program also 
generates random passwords such as "password", "12345678", 
and "iloveyou"
'''

import os
import string
import random
import csv

def password_maker(): 
    
    output = {}
    
    commonPassInds = []
    commonPass = ["password", "12345678", "iloveyou"] 
    allowedChar = (string.ascii_uppercase + string.ascii_lowercase) 
    
    #string.digits)
    
    for i in range(100):
    	password = []
    	for j in range(8):
    		password.append(random.choice(allowedChar))
    	passwordStr = "".join(password)
    	userStr = "user" + str(i)
    	output[userStr] = passwordStr
    
    for i in range(10):
    	ind = random.randint(1,99)
    	commonPassInds.append(ind)
    
    for i in range(len(commonPassInds)):
    	index = commonPassInds[i]
    	userStr = "user" + str(index)
    	passwordStr = random.choice(commonPass)
    	output[userStr] = passwordStr
    	
    return output