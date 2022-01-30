#https://www.delftstack.com/howto/python/python-generate-prime-number/#:~:text=Under%20the%20Python%20random%20module%2C%20it%20has%20a,prime%20number%20within%20the%20list%20using%20random.choice%20%28%29.

#https://www.tutorialspoint.com/How-to-generate-prime-numbers-using-Python
import random 

import math 

def prime_range_generator(start,end):
    
    prime_list = [] 
    
    for x in range(start,end):
        
        for y in range(2,x):
            
            if x%y == 0:
                
                break 
            
            else:
                
                prime_list.append(x)
                
    prime_list = set(prime_list)   
    
    prime_list = list(prime_list) 
    
    print(prime_list) 
            
    return prime_list 
  
def creating_N():
    
    prime_list = prime_range_generator(1,1000)
    
    value_one = random.randint(0,20)
    
    value_two = random.randint(0,20) 
    
    p = prime_list[value_one] 
    
    q = prime_list[value_two]
    
    N = p * q 
    
    print("p",p) 
    
    print("q",q) 
    
    key = [N,p,q] 
    
    print(p,q,N)
    
    return key
  
 #https://www.wolframalpha.com/calculators/factoring-calculator/
  
def key_builder():
    
    key = creating_N() 
    
    N = key[0] 
    
    p = key[1] 
    
    q = key[2] 
    
    phi = (p-1) * (q-1) 
    
    e = 0 
    
    d = 0 
    
    list_of_values = [] 

    for x in range(1,20):
        value = (phi*x)+1 
        if value % phi == 1:
            list_of_values.append(value) 
        
    print("list of values",list_of_values)
    
    index = random.randint(0,len(list_of_values)-1) 

    digit = list_of_values[index] 

    print("digit",digit) 
    x = digit/2 
    print("x = digit/2",x) 
    x = math.ceil(x) 
    print("x = digit/2 with ceil",x) 
    x = int(x) 
    print("x (int)",x) 
    i = 0 
    for i in range(2,x):
        if(digit % i == 0): 
            print("digit",digit) 
            print("digit % i",i) 
            break 

    k = digit/i 
    
    print("i",i)
    
    print("k",k)
    
    e = i 
    
    d = k 

    print("e = ",e) 
    
    print("d = ",d)
    
    print("phi = ",phi) 
    
    print("N = ",N) 
    
    public_key = [e,N] 
    
    private_key = [p,q,d]
    
    return public_key
    

        
        
    
    
    
#https://stackoverflow.com/questions/19850283/how-to-generate-rsa-keys-using-specific-input-numbers-in-openssl
    
    
#public_key,private_key = key_maker() 
