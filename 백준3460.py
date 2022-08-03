import sys
input=sys.stdin.readline
n = int(input())
for _ in range(n):
    i = 0
    while n > 0:
        if n%2 == 1:
            print(i, c=' ')
        n = n//2
        i += 1