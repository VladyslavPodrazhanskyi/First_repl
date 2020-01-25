# Дан список целых чисел, число k и значение C.
# Необходимо вставить в список на позицию с индексом k элемент, равный C, сдвинув все элементы,
# имевшие индекс не менее k, вправо.
# Поскольку при этом количество элементов в списке увеличивается,
# после считывания списка в его конец нужно будет добавить новый элемент, используя метод append.
# # Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе и не создавая дополнительного списка.

#  1 решение -  не догадался добавить сразу нулевой элемент в конце
# и в случае, когда элемент вставлялся в конец пришлось описывать в отдельном условии.
numbers = [int(x) for x in input().split()]
k, C = [int(y) for y in input().split()]
if k < len(numbers):
    last_el = numbers[len(numbers) - 1]
    for i in range(len(numbers) - 1, k, -1):
        numbers[i] = numbers[i - 1]
    numbers[k] = C
    numbers.append(last_el)
else:
    numbers.append(C)
print(' '.join([str(x) for x in numbers]))

numbers = [int(x) for x in input().split()]
k, C = [int(y) for y in input().split()]

numbers.append(0)
for i in range(len(numbers) - 1, k, -1):
    numbers[i] = numbers[i - 1]
numbers[k] = C
print(' '.join([str(number) for number in numbers]))