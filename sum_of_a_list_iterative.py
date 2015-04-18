#calculate the sum of a list iteratively

def listnum(numList):
    theSum = 0 
    
    for i in numList:
        theSum += i
        
    return theSum

#test the function
alist = [1,3,5,7,9]
listnum(alist)
