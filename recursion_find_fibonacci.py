#find fibonacci number in the series by recursion

def findFib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return findFib(n-1)+ findFib(n-2)
        

#test the code
findFib(10)
