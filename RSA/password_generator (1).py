#Resource is https://pynative.com/python-generate-random-string/#h-steps-to-create-a-random-string

#Generating passwords based on cahllenge number (edited)
import string 

import random 

def password_maker(): 
        
    letters_of_ascii = string.ascii_letters
    
    password_list = [] 
    
    number_of_passwords = 2 
    
    for x in range(number_of_passwords): 
        
        key_length = 8 
        
        key = ''.join(random.choice(letters_of_ascii) for i in range(key_length))
        
        password_list.append(key) 
        
    return password_list 