def duplicate(ls,n):
    ans = False
    ''' input:ls-List of elements and n-indicates the length of list
         output:Return ans as True or False'''
    
    # YOUR CODE GOES HERE
    for i in range(len(ls)-1):
        if ls[i] == ls[i+1]:
            return True

    
    return ans
