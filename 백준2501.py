
import sys
input=sys.stdin.readline
arr=[]
n,m = map(int, input().split())

c = 0
for i in range(1, n + 1):
    if n % i == 0:
        arr.append(i)
    c += 1

if m > len(arr):
    print(0)
else:
    print(arr[m-1])