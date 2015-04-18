#recursive algorithm  for finding factorial of an integer

def findFac(number):
    
    if number < 2: 
        return 1
    else:
        return number * findFac(number-1)
        
        

#test the code
findFac(3)
findFac(1)
findFac(2)
findFac(4)
