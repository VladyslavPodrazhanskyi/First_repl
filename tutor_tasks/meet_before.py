# Во входной строке записана последовательность чисел через пробел.
# Для каждого числа выведите слово YES (в отдельной строке),
# если это число ранее встречалось в последовательности или NO, если не встречалось.

# My first ugly solution:

# list_num = input().split()
# print('NO')
# for i in range(1, len(list_num)):
#     if list_num[i] in set(list_num[:i]):
#         print('YES')
#     else:
#         print('NO')

# My second solution similar to the solution of developers:

list_num = input().split()
meet_before = set()

for el in list_num:
    if el in meet_before:
        print('YES')
    else:
        print('NO')
        meet_before.add(el)
