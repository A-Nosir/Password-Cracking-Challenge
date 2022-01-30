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

import password_generator 

import symmetric_encryption

password_list = password_generator.password_maker() 

print("Password List:",password_list) 

upper_key,lower_key = symmetric_encryption.shift(3)

encrypted_passwords = []

for user_name in password_list: 
    
    password = password_list[user_name] 
    
    encrypted_password = symmetric_encryption.translator(upper_key,lower_key,password) 
    
    encrypted_passwords.append(encrypted_password) 
    
print("Encrypted Passwords",encrypted_passwords) 
    
encrypted_password_list = open("encrypted_password_list.txt","w")

for encrypted_password in encrypted_passwords:
    
    encrypted_password_list.write(encrypted_password + "\n")
    