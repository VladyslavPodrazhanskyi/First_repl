# Шахматная ладья ходит по горизонтали или вертикали. Даны две различные клетки шахматной доски, определите, может ли ладья попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести YES, если из первой клетки ходом ладьи можно попасть во вторую или NO в противном случае..

col_1 = int(input())
str_1 = int(input())
col_2 = int(input())
str_2 = int(input())

if col_1 == col_2 or str_1 == str_2:
    print('YES')
else:
    print('NO')