#algorithm for getting the reverse of a string

#easy Pythonic way would be astring[::-1] but here I try an algorithm using Stack data structure

from pythonds.basic.stack import Stack

def revString(astring):
    s = Stack() #create a new stack
    
    for ch in astring:
        s.push(ch)
    
    reverse_string = ''

    for i in range(len(astring)):
        reverse_string = reverse_string + s.pop()
        
    return reverse_string
    
#test the code
revString('this is the string to be reversed')
