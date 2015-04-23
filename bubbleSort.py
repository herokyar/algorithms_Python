#bubble sort algorithm in python
#a nice algorithm to sort a list of numbers

def bubbleSort(alist):
    
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                #this is the part of the swap (use a temp variable)
                temp = alist[i]    
                alist[i] = alist[i+1]
                alist[i+1] = temp
                

#test the algorithm
alist = [54,26,93, 17,77,31,44]
bubbleSort(alist)
print alist
