#За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? Программа получает на вход числа n и m.

from math import ceil
n = int(input())
m = int(input())

print(ceil(m/n))
#if m % n == 0:
 #   print(m//n)
#else:
#   print(m//n + 1) 
