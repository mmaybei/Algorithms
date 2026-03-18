import sys

n = int(sys.stdin.readline())

array = []
for _ in range(n):
    array.append(int(sys.stdin.readline()))

array.sort()

for num in array:
    sys.stdout.write(str(num) + '\n')