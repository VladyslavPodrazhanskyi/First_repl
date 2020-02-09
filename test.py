n = int(input())
words = set()

for i in range(n):
    words.update(set(input().split()))
print(len(words))
