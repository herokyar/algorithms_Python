

#recursive algorithm to reverse a list

def revList(alist):
    
    if len(alist) < 2:
        return alist
    else:
        return [alist[-1]] + revList(alist[:-1]) #important, turn the first element into a list
        
#test the algorithm
revList([1,2,3])
revList([1,2,3,4,5])
