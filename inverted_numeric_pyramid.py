N = int(input())

for row in range(N, 0, -1):
    for col in range(1, row+1):
        if col < row:
            print(col, end=' ')
        else:
            print(col, end='')
    print()
