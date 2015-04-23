#stop bubble sort algorithm early is the list is sorted
#this algorithm is more effective than the bubble sort algorithm

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum -1
    
    
#test the code
alist = [20,30,40,90,50,60,70,80,100]
shortBubbleSort(alist)
print alist
