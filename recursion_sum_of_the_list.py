#calculate the sum of the list using recursion

def listsum(numList):
    
    if len(numList) == 1: #this is the special case, where there is only one item in the list
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])
    
    
    
#test the code
listsum([1,3,5,7])

