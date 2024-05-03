t = int(input("Enter the number of test cases(t): "))    # no of test cases
for i in range(t):
    A = []
    n = int(input("Enter no. of elements in the array(n): "))  # total no of elements in the list
    for j in range(n):
        A.append(int(input("Enter element: ")))    # appending each elements in the list

    print(A)    # print final list

    count_neg = 0
    count_zero = A.count(0)    # count function used to count if list has 0

    if count_zero > 0:
        print(0)   
    else:
        pointer = 0
        while pointer < n:
            if A[pointer] < 0:
                count_neg += 1
            pointer += 1
            
        if count_neg % 2 != 0:
            print(1)
        else:
            print(0)
