#Дано трехзначное число. Найдите сумму его цифр.

num = int(input())

num_3 = num // 100
num_2 = num % 100 // 10
num_1 = num % 10

print (num_3 + num_2 + num_1)

# Решение разработчиков

n = int(input())
a = n // 100
b = n // 10 % 10
c = n % 10
print(a + b + c)