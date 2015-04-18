#recursion algorithm for binary search of an item in a list

def binarySearch(alist, item):
    
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item<alist[midpoint]:
                return binarySearch(alist[:midpoint],item)
            else:
                return binarySearch(alist[midpoint+1:], item)
            

#test the code
testlist = [1,2,3,4,5,44,55,66]
binarySearch(testlist,3)
binarySearch(testlist,45)
