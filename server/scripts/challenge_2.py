import string
import random

# Challenge 2 - Caesar Cipher
# Author: Justin Tareq

'''
Name: Justin Tareq 
Class: COMP 3109 
Source: https://www.udemy.com/course/learn-modern-security-and-cryptography-by-coding-in-python/learn/lecture/20065642?start=0#overview
 
Purpose of Program: The source code is to shift ascii values by 3 as 
part of Caesar's Cipher, a method invented by the Roman ruler Julius
Caesar. This program summons codes from password_generator.py 
and symmetric_encryption.py. After it gets the generated passwords at 
length eigth, it will encrypt them and write the encrypted passwords 
into a file. 
'''

def shift(n):
	counter = 0 
	
	upper_key = {}  
	lower_key = {} 

	uppercase_letters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
	lowercase_letters = "0123456789abcdefghijklmnopqrstuvwxyz" 

	for c in uppercase_letters:    
		upper_key[c] = uppercase_letters[(counter + n) % len(uppercase_letters)]  
		counter += 1
		
	for c in lowercase_letters: 
		lower_key[c] = lowercase_letters[(counter + n) % len(lowercase_letters)]
		counter += 1 
		
	return upper_key,lower_key 
	
def translator(upper_key,lower_key,msg): 
	cipher = "" 
	
	for c in msg:
		if c.islower() and c in lower_key: 
			cipher += lower_key[c]; 
			
		if c.isupper() and c in upper_key: 
			cipher += upper_key[c] 
			
		if c.isdigit() and c in lower_key and c in upper_key: 
			cipher += upper_key[c] 
			
	return cipher  

def password_maker(cnum):

	random.seed(cnum) 
	
	output = {}
	
	commonPassInds = []
	commonPass = ["password", "12345678", "iloveyou"] 
	allowedChar = (string.ascii_uppercase + string.ascii_lowercase) 
	
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

def get_challenge_set(cnum):

	secret = 24343423
	secret = int(str(secret ** int(cnum))[0:2])

	password_list = password_maker(secret)

	upper_key, lower_key = shift(secret)

	outputList = []

	for user_name in password_list: 
		encrypted_password = translator(upper_key, lower_key, password_list[user_name]) 
		outputList.append({
			"username": user_name, 
			"password": encrypted_password
		})

	return outputList

def validate_attempt(cnum, username, password):
	secret = 24343423
	secret = int(str(secret ** int(cnum))[0:2])

	password_list = password_maker(secret)

	if (username in password_list):
		return password == password_list[username]
	else:
		return False
