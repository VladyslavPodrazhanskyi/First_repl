a = int(input())
b = int(input())
try:
  print(a/b)
except ZeroDivisionError:
  print('На нуль делить нельзя!')