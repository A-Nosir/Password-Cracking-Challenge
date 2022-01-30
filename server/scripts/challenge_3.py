# double DES Encryption
import string
import random
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from secrets import token_bytes

# Challenge 3 - Double DES
# Author: David Li, Saul Hughes

#DES encryption with feistel cipher
def des_encrypt(msg, key):
    cipher = DES.new(bytes(key), DES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(msg.encode('ascii'), DES.block_size))

    return ciphertext

#Double DES encryption
def double_des_encrypt(msg, key, key2):
    ciphertext = des_encrypt(msg, key)
    doubleDES = des_encrypt(str(ciphertext), key2)

    return doubleDES.hex();

# Returns a list of dictionaries with keys username and password
def get_challenge_set(cnum):

    # Generate a secret int using secret and cnum
    secret = 23479
    secret = int(str(secret ** int(cnum))[0:8])

    # We will always get the same challenge set for a given cnum
    random.seed(secret)

    key1 = random.randbytes(8)
    key2 = random.randbytes(8)

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

    outputList.append({
        "username": "user0",
        "plaintext": "",
        "password": double_des_encrypt(output["user0"], key1, key2)
    })

    for key in output:
        outputList.append({
            "username": key,
            "plaintext": output[key],
            "password": double_des_encrypt(output[key], key1, key2)
        })

    return outputList

def validate_attempt(cnum, username, password):
    # Generate a secret int using secret and cnum
    secret = 23479
    secret = int(str(secret ** int(cnum))[0:8])

    # We will always get the same challenge set for a given cnum
    random.seed(secret)

    key1 = random.randbytes(8)
    key2 = random.randbytes(8)

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

    outputList.append({
        "username": "user0",
        "plaintext": "",
        "password": double_des_encrypt(output["user0"], key1, key2)
    })

    for key in output:
        outputList.append({
            "username": key,
            "plaintext": output[key],
            "password": double_des_encrypt(output[key], key1, key2)
        })

    if (username == "user0"):
        return password == outputList[0]["password"]
    else:
        return False
