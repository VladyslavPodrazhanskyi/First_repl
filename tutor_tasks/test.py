# Connection for loop and while loop
# s = 'kfjaoruewuroijfgioer'
#
# for el in s:
#     print(el + '*', end='')
# print('\n')
#
# i = 0
# while i < len(s):
#     print(s[i] + '*', end='')
#     i += 1

# Fibonacci with recursion:
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
# for i in range(2, 11):
#     print(fib(i))

# Fibonacci with for loop:
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        second_prev, prev = 0, 1
        for i in range(n-1):
            fib = second_prev + prev
            second_prev, prev = prev, fib
        return fib

for i in range(2, 11):
    print(fib(i))