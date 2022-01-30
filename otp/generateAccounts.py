import os
import string
import random
import csv

outputFile = "./plaintext-xxx.csv"
output = {}

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

with open(outputFile, "w") as csv_file:
	f = csv.writer(csv_file)
	for key in output:
		row = [key, output[key]]
		f.writerow(row)
