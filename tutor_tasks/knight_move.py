# Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом направлении и на одну клетку по горизонтали, или наоборот. Даны две различные клетки шахматной доски, определите, может ли конь попасть с первой клетки на вторую одним ходом.

col_1 = int(input())
str_1 = int(input())
col_2 = int(input())
str_2 = int(input())
dcol = abs(col_1 - col_2)
dstr = abs(str_1 - str_2)

if dcol == 1 and dstr == 2 or dcol == 2 and dstr == 1:
    print('YES')
else:
    print('NO')