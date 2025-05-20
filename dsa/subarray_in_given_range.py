# Given an array A of length N, return the subarray from B to C.
A = [4, 3, 2, 6]
B = 1
C = 3

res = []
        
while B <= C:
    res.append(A[B])
    B += 1

print(res)
