#algorithm for making a prime number list from (1,100)

import math #import the math module

def isPrime(n):
    
    if n<= 1: 
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for t in range(3, int(math.sqrt(n)+1), 2): #this is the more general case for finding a prime number
        if n%t == 0:
            return False
    return True

#test the algorithm
primeList = [n for n in range(100) if isPrime(n)]
print primeList
