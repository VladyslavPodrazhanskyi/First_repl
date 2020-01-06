# Дана строка, в которой буква h встречается минимум два раза.
# Удалите из этой строки первое и последнее вхождение буквы h,
# а также все символы, находящиеся между ними

s = input()
ind_1 = s.find('h')
ind_2 = s.rfind('h')
print(s[:ind_1] + s[ind_2 + 1:])

# solution of developers (is not better than mine):

s = input()
part_1 = s[:s.find('h')]
part_2 = s[s.rfind('h') + 1:]

print(part_1 + part_2)