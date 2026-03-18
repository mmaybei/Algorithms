from bisect import bisect_left, bisect_right

import sys
input = sys.stdin.readline

n = int(input())
a_list = list(map(int, input().split()))
m = int(input())
b_list = list(map(int, input().split()))

a_list.sort()

for b in b_list:
    count = bisect_right(a_list, b) - bisect_left(a_list, b)
    print(count, end=' ')