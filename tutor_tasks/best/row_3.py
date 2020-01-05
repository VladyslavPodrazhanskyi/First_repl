#Даны два целых числа A и В, A>B.
# Выведите все нечётные числа от A до B включительно,
# в порядке убывания. В этой задаче можно обойтись без инструкции if.

a = int(input())
b = int(input())

for i in range(a - 1 + a % 2, b - 1, -2):
    print(i, end=' ')

# Решение разработчиков

a = int(input())
b = int(input())
for i in range(a - (a + 1) % 2, b - b % 2, -2):
    print(i, end=' ')
