#Яша плавал в бассейне размером N × M метров и устал. В этот момент он обнаружил, что находится на расстоянии x метров от одного из длинных бортиков (не обязательно от ближайшего) и y метров от одного из коротких бортиков. Какое минимальное расстояние должен проплыть Яша, чтобы выбраться из бассейна на бортик? Программа получает на вход числа N, M, x, y. Программа должна вывести число метров, которое нужно проплыть Яше до бортика.

N = int(input())
M = int(input())
x = int(input())
y = int(input())
short_board, long_board = min(N, M), max(N, M)
min_dist = min(x, short_board - x, y, long_board - y )
print(min_dist)

# Решение только с использованием условных конструкций:
N = int(input())
M = int(input())
x = int(input())
y = int(input())
if N < M:
    short_board, long_board = N, M
else:
    short_board, long_board = M, N
if x > short_board - x:
    x = short_board - x
if y > long_board - y:
    y = long_board - y
if x < y:
    print(x)
else:
    print(y)