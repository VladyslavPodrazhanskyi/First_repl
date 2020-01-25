# Дан текст: в первой строке задано число строк, далее идут сами строки.
# Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке

# # First solution
# words = []
# freq_dict = dict()
# for _ in range(int(input())):
#     current_words = input().split()
#     words.extend(current_words)
# for word in words:
#     freq_dict[word] = freq_dict.get(word, 0) + 1
# most_freq_list = [k for k, v in freq_dict.items() if v == max(freq_dict.values())]
# print(min(most_freq_list))

import collections

words = []
for _ in range(int(input())):
    current_words = input().split()
    words.extend(current_words)
counter = collections.Counter(words)
most_freq = [k for k, v in counter.items() if v == max(counter.values())]
print(min(most_freq))

