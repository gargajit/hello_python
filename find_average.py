t = int(input())   #tests cases         
for i in range(t):          
    A, C = map(int, input().split())  #two integer inputs
    if A % 2 == 0 and C % 2 == 0 or A % 2 != 0 and C % 2 != 0:
        B = int((A + C) / 2)
    else:
        B = -1
    print(B)    #integer output
        
