import string
import random

# Challenge 1 - One Time Pad
# Author: Saul Hughes

# Obtained from challenge 1 instructions
def encrypt(pad,msg):
	return bytes([x^ord(y) for (x,y) in zip(pad,msg)]).hex()

# Returns a list of dictionaries with keys username and password
def get_challenge_set(cnum):

	# Generate a secret int using secret and cnum
	secret = 23479
	secret = int(str(secret ** int(cnum))[0:8])

	# We will always get the same challenge set for a given cnum
	random.seed(secret)
	
	pad = bytes(random.getrandbits(8) for _ in range(8))

	output = {}
	outputList = []
	commonPassInds = []
	commonPass = ["password", "12345678", "iloveyou"] 
	allowedChar = (string.ascii_uppercase + string.ascii_lowercase + string.digits)

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

	for key in output:
		outputList.append({
			"username": key, 
			"password": encrypt(pad, output[key])
		})

	return outputList

def validate_attempt(cnum, username, password):
	if (username == "user100" and password == "demopassword"):
		return True
	
	# Generate a secret int using secret and cnum
	secret = 23479
	secret = int(str(secret ** int(cnum))[0:8])

	# We will always get the same challenge set for a given cnum
	random.seed(secret)
	
	pad = bytes(random.getrandbits(8) for _ in range(8))

	output = {}
	outputList = []
	commonPassInds = []
	commonPass = ["password", "12345678", "iloveyou"] 
	allowedChar = (string.ascii_uppercase + string.ascii_lowercase + string.digits)

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

	for key in output:
		outputList.append({
			"username": key, 
			"password": output[key]
		})
	
	if (username == "user0"):
		return password == output["user0"]
	else:
		return False
