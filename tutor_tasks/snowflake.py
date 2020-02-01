# Дано нечетное число n. Создайте двумерный массив из n×n элементов, заполнив его символами "."
# (каждый элемент массива является строкой из одного символа).
# Затем заполните символами "*" среднюю строку массива, средний столбец массива,
# главную диагональ и побочную диагональ. В результате единицы в массиве должны образовывать
# изображение звездочки. Выведите полученный массив на экран, разделяя элементы массива пробелами.

# 1st solution:
# n = int(input())
# massive = [['.']*n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i == (n // 2) or j == (n // 2) or i == j or i + j == (n - 1):
#             massive[i][j] = '*'
#
# for i in range(n):
#     print(' '.join(massive[i]))

# 2nd solution ( is equal to the solution of the developers

n = int(input())

massive = [['.']*n for _ in range(n)]

for i in range(n):
    massive[i][i] = '*'
    massive[n // 2][i] = '*'
    massive[i][n // 2] = '*'
    massive[i][n - i - 1] = '*'

for row in massive:
    print(' '.join(row))



