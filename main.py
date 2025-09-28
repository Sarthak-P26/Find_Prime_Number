def finding_prime(num):
    for numbers in range(2, num-1):
        if num == 2:
            print(f"{num} is a prime number")
        elif num % numbers == 0:
            print(f"{num} is not a prime number")
        
    
            
                