# Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:
# Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.
# Числа, стоящие выше этой диагонали, равны 0.
# Числа, стоящие ниже этой диагонали, равны 2.
# Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.

n = int(input())

massive = [[0] * n for _ in range(n)]
# second solution
for i in range(n):
    massive[i] = [0] * (n - i - 1) + [1] + [2] * i

# 1st solution
# for i in range(n):
#     for j in range(n):
#         if i+j == n-1:
#             massive[i][j] = 1
#         elif i+j > n-1:
#             massive[i][j] = 2

for row in massive:
    print(' '.join([str(el) for el in row]))
