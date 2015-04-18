

from pythonds.basic.stack import Stack

rStack = Stack() #create a new stack object

def toStr(n, base):
    
    convertString = '0123456789ABCDEF'
    
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])
            
        n = n // base #update n
        
    res = '' #empty string
    
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
        
    return res
        

#test the algorithm
toStr(77,10)
toStr(1459,16)
