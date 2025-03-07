# Given an integer N as input
# Print perfect squares till N

N = int(input())

# Simple Way

# cnt = 1

# while cnt <= N:
#   if cnt ** 2 <= N:
#     print(cnt ** 2, end = ' ')
#     cnt += 1
#   else:
#     break


# Smart Way

cnt = 1

while cnt ** 2 <= N:
  print(cnt ** 2, end = ' ')
  cnt += 1
