'''
Name: Justin Tareq 

Class: COMP 3109 

Source: https://www.udemy.com/course/learn-modern-security-and-cryptography-by-coding-in-python/learn/lecture/20065642?start=0#overview
 
Purpose of Program: The source code is to shift ascii values by 3 as 
part of Caesar's Cipher, a method invented by the Roman ruler Julius
Caesar. The programs encrypts passwords with lowercase letters,
uppercase letters, and digits through shifting them by 3. During the 
summer, this was code I typed while taking a cryptography course on 
Udemy by Rune Thompson which is: Learn Modern Secrity and Cryptography 
By Coding In Python. 
''' 


#https://www.udemy.com/course/learn-modern-security-and-cryptography-by-coding-in-python/learn/lecture/20065642?start=0#overview

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