# Август и Беатриса продолжают играть в игру, но Август начал жульничать.
# На каждый ивсе числа, которые мог загадать Август после ответа на все вопросы Беатрисы.
# Из вопросов Беатрисы он выбирает такой вариант ответа YES или NO, чтобы множество возможных задуманных чисел
# оставалось как можно больше. Например, если Август задумал число от 1 до 5,
# а Беатриса спросила про числа 1 и 2, то Август ответит NO, а если Беатриса спросит про 1, 2, 3,
# то Август ответит YES.
# #
# # Если же Бетриса в своем вопросе перечисляет ровно половину из задуманных чисел,
# то Август из вредности всегда отвечает NO. Наконец, Август при ответе учитывает все
# предыдущие вопросы Беатрисы и свои ответы на них, то есть множество возможных задуманных чисел уменьшается.
# #
# # Первая строка содержит наибольшее число, которое мог загадать Август.
# Каждая следующая строка содержит очередной вопрос Беатрисы: набор чисел, разделенных пробелами.
# Последняя строка входных данных содержит одно слово HELP.
# #
# # Для каждого вопроса Беатрисы выведите ответ Августа на этот вопрос.
# После этого выведите через пробел, в порядке возрастания,

possible_nums = {num for num in range(1, int(input()) + 1)}
guess = input()
while guess != 'HELP':
    guess_nums = {int(x) for x in guess.split()}
    if len(possible_nums & guess_nums) > len(possible_nums - guess_nums):
        print('YES')
        possible_nums &= guess_nums
    else:
        print('NO')
        possible_nums -= guess_nums
    guess = input()
#print(' '.join([str(el) for el in sorted(possible_nums)]))
print(*sorted(possible_nums))