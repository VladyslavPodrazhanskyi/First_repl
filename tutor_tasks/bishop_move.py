# Шахматный слон ходит по диагонали. Даны две различные клетки шахматной доски, определите, может ли слон попасть с первой клетки на вторую одним ходом.

col_1 = int(input())
str_1 = int(input())
col_2 = int(input())
str_2 = int(input())

if col_1 + str_1 == col_2 + str_2 or col_1 - str_1 == col_2 - str_2:
    print('YES')
else:
    print('NO')

# developers solution:
# эти решения эквивалентны, так как можно доказать, что 
# bs(x1 - x2) == abs(y1 - y2)
# эквивалентно -  (x1 + y1)==(x2 + y2) or (x1 - y1)==(x2 - y2)
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2):
    print('YES')
else:
    print('NO')