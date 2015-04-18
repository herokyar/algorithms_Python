#recursion convert any number to string
#in any base

def toStr(n, base):
    convertString = '0123456789ABCDEF'
    
    if n < base: #base case
        return convertString[n]
    else:
        return toStr(n//base,base) + convertString[n%base]
        
       
    
#test the code
toStr(768, 10)
toStr(7, 10)
