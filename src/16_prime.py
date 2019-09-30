# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter One number:  ")

def prime(x):
    if int(x) > 1:  ## if passed in number is greater than one
        
        # Iterate from 2 to n / 2  
        for i in range(2, int(x)//2):         
                # If x is divisible by any number between  
                # 2 and n / 2, it is not prime  
            if (int(x) % i) == 0: 
                print(f"{x} is not a prime number") 
                break
                    
        else: 
            print(f"{x} is a prime number") 
            
    else: 
        print(x, "is not a prime number") 

prime(x)