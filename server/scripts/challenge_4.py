import string
import random

# Challenge 4 - RSA
# Author - Saul Hughes

primes = [11261, 27299, 13297, 6781, 28901, 86509, 52517, 34537, 56999, 84787,
97423, 54287, 19157, 14543, 20641, 93949, 21557, 41143, 11987, 7309, 70379,
44537, 82549, 70621, 79811, 24989, 58369, 79669, 73517, 337, 57191, 16103,
41413, 28547, 47981, 10889, 13789, 62981, 73369, 85411, 75347, 39877, 7591, 563,
12037, 34147, 5413, 66191, 52103, 17573]

def encrypt(p, q, msg):
	N = p*q
	e = random.randint(1, ((p-1)*(q-1))-1)

	return "".join([ hex(pow(ord(m), e, N)) for m in msg ])

def get_challenge_set(cnum):

	# Generate a secret int using secret and cnum
	secret = 23479
	secret = int(str(secret ** int(cnum))[0:8])

	# We will always get the same challenge set for a given cnum
	random.seed(secret)

	p = primes[random.randint(0, 49)]
	q = primes[random.randint(0, 49)]

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
			"password": encrypt(p, q, output[key])
		})

	return outputList

def validate_attempt(cnum, username, password):
	# Generate a secret int using secret and cnum
	secret = 23479
	secret = int(str(secret ** int(cnum))[0:8])

	# We will always get the same challenge set for a given cnum
	random.seed(secret)

	p = primes[random.randint(0, 49)]
	q = primes[random.randint(0, 49)]

	output = {}
	outputList = []
	allowedChar = (string.ascii_uppercase + string.ascii_lowercase + string.digits)

	for i in range(100):
		password = []
		for j in range(8):
			password.append(random.choice(allowedChar))
		passwordStr = "".join(password)
		userStr = "user" + str(i)
		output[userStr] = passwordStr

	if (username in output):
		return password == output[username]
	else:
		return False