import rsa 

#https://www.cs.drexel.edu/~jpopyack/IntroCS/HW/RSAWorksheet.html

import password_generator 

#Saul_Hughes_Password_Generator

def convert_to_ascii_string(word): 
    number = "" 
    for x in word: 
        number += str(ord(x)) 
    return number 


public_key = []

password_list = [] 
    
public_key = rsa.key_builder()

password_list = password_generator.password_maker() 

print("PASSWORD LIST",password_list) 

print(public_key)

print(password_list) 

#Modify each password to their ascii values 

password_ascii_list = [] 

for word in password_list:
    password = convert_to_ascii_string(word) 
    password_ascii_list.append(password) 
    
'''for user in password_list: 
    word = password_list.get(user) 
    value = convert_to_ascii_string(word)
    value = int(value) 
    password_ascii_list.append(value) ''' 

print(password_ascii_list) 
    
encrypted_values = [] 

#Encrypt it with the public key provided 
    #Generate a list with the encrypted values with pow 
    #Write the encrypted values into a file 
    
e = public_key[0]
    
N = public_key[1] 
    
encrypted_passwords = open("encrypted_passwords.txt","w")
    
for value in password_ascii_list:
    
    value = int(value) 
        
    encryption = pow(value,e) % N 
        
    print("Encryption : ",encryption) 
    
    encrypted_values.append(encryption) 
    
    encryption = str(encryption)
        
    encrypted_passwords.write(encryption) 
        
    #999961
    
    
    
    




    
    
  






        
    