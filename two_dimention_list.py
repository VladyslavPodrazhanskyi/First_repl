n = int(input('Please imput size of the massive: '))
massive = [[0]*n for _ in range(n)]

# 1st solution with using double loop and and if conditions:

# for i in range(n):
#     for j in range(n):
#         if j == i:
#             massive[i][j] = 1
#         elif j > i:
#             massive[i][j] = 0
#         else:
#             massive[i][j] = 2

# 2nd solution with one loop:

# for i in range(n):
#     massive[i][i] = 1
#     for j in range(0, i):
#         massive[i][j] = 2
#     for j in range(i + 1, n):
#         massive[i][j] = 0

# 3rd solution:

# for i in range(n):
#     massive[i] = [2]*i + [1] + [0]*(n - i - 1)

# 4th solution:

massive = [[2]*i + [1] + [0]*(n - i - 1) for i in range(n)]



for row in massive:
    print(' '.join([str(el) for el in row]))



