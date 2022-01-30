import os
import csv

inputFile = "./plaintext-xxx.csv"
outputFile = "./ciphertext-xxx.csv"

# Obtained from challenge 1 instructions
def encrypt(pad,msg):
	return bytes([x^ord(y) for (x,y) in zip(pad,msg)]).hex()

pad = os.urandom(8)

with open(inputFile) as csv_file:
	f = csv.reader(csv_file)
	input = dict(f)

output = {}

for key in input:
	output[key] = encrypt(pad, input[key])

with open(outputFile, "w") as csv_file:
	f = csv.writer(csv_file)
	for key in output:
		row = [key, output[key]]
		f.writerow(row)
