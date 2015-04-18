#reverse a string usign recursion

def reverse(s):
    
    if len(s) == 1: #base case recursion
        return s
    elif len(s) == 0: #also consider where lenght is 0
        return ''
    else:
        return s[-1] + reverse(s[:-1])
        

#test the function
reverse('abc')
reverse('a')
reverse('')
