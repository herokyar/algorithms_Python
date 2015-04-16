#multiply every number in a list with each other and return the result


def mulList(alist):
    s = 1 #initial value
    
    for n in alist:
        s = s * n
        
    return s
    

#test the code
newlist = [3,4,5,6] #create a new list
mulList(newlist)

