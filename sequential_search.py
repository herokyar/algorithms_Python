#sequential search algorithm of an unordered list:

#complexity big-O(n)  #worst case
#big-O(1) if the item is at the beginning

def sequentialSearch(alist, item):
    
    pos = 0
    found = False
    
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1
            
    return found
    
