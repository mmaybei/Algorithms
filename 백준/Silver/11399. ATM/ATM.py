import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
array.sort()

result = 0
for i in range(len(array)):
    result += array[i] * (n - i)

print(result)