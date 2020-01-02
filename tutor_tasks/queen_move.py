# Шахматный ферзь ходит по диагонали, горизонтали или вертикали. Даны две различные клетки шахматной доски, определите, может ли ферзь попасть с первой клетки на вторую одним ходом.

col_1 = int(input())
str_1 = int(input())
col_2 = int(input())
str_2 = int(input())

if col_1 == col_2 or str_1 == str_2 or abs(col_1 - col_2) == abs(str_1 - str_2):
    print('YES')
else:
    print('NO')