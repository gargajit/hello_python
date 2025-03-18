def first_multiple(ls,x):
    ans = -1
    ''' input:ls-List of elements and x-indicates the integer
         output:Return ans from the list that is divisible by x'''
    
    # YOUR CODE GOES HERE
    for num in ls:
        if num % x == 0:
            return num
    
    return ans
