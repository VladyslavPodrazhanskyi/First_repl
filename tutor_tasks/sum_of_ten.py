# Дано 10 целых чисел. Вычислите их сумму.
# Напишите программу, использующую наименьшее
# число переменных.

summa = 0
for i in range(10):
    summa += int(input(f'input number {i + 1}: '))
print(summa)