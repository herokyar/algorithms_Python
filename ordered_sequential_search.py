#ordered sequential search of a list 

def orderedSequentialSearch(alist, item):
    
    pos = 0
    found = False
    stop = False
    
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos]  > item:
                stop = True
            else:
                pos = pos + 1
                
    return found
    
    
#test the algorithm
testlist = [17, 19, 32, 42]
orderedSequentialSearch(testlist, 32)
