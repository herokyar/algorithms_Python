#algorithm to reverse a string iteratively

def reverse(input):
    return ''.join([input[i] for i in range(len(input)-1, -1, -1)])
    
    #range(len(input)-1, -1, -1) is a nice way to index the string backwords

#test the code
s = 'this is my string'
reverse(s)  
