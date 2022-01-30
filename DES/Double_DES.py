# double DES Encryption
import random
from Crypto.Cipher import DES
from secrets import token_bytes 

#generate a secret 64bits secret key base on a challenge number
def generate_key(challenge_num):

    random.seed(challenge_num)
    key = random.randbytes(8)

    return key


#DES encryption with feistel cipher
def des_encrypt(msg, key):
    cipher = DES.new(bytes(key), DES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))

    return ciphertext

#Double DES encryption
def double_des_encrypt(msg, key, key2):
    ciphertext = des_encrypt(msg, key)
    doubleDES = des_encrypt(str(ciphertext), key2)

    return doubleDES;
