import sys
input=sys.stdin.readline
list=[]
n=int(input())
for i in range(n):
    a,b = map(int,input().split())
    list.append((a,b))
list.sort()
for i in range(n):
    print(list[i][0],list[i][1])