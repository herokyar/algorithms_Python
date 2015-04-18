#iterative algorithm to find Fibonacci sequence

def findFib(n):
    
    fibList = [1,1] #beginning of the list
    
    for i in range(n-2):
        fibList.append(fibList[-1]+fibList[-2])
        
    return fibList      
    
#algorithm complexity big-O(n)


#test the code
findFib(10) #find the first 10 numbers 
