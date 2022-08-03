import sys
input=sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
max = num[0]
min = num[0]
for i in num:
    if i > max:
        max = i
    elif i < min:
        min = i
print(min, max)