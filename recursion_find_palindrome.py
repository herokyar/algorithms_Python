#find palindrome in a strign (use recursion)

#this helper function removes whitespaces, special chars and also lowercase all
def removeWhite(s):
    
    s = s.lower()
    s = s.replace(' ', '').replace('’', '').replace(',','') #remove special chars
    
    return s
    

#here is the main function
def isPal(s):
    
    s = removeWhite(s)
    
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    
    return isPal(s[1:-1])
    
    
#test the function
isPal('a')
isPal('radar')
isPal('MAdam i’m adam') #this also returns True
