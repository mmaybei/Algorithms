import sys
input = sys.stdin.readline

n = int(input())

words = set()

for _ in range(n):
    words.add(input().rstrip('\n'))

sorted_list = [[] for _ in range(51)]

for word in words:
    sorted_list[len(word)].append(word)

for words in sorted_list:
    if len(words) > 1:
        words.sort()

for words in sorted_list:
    for word in words:
        print(word)