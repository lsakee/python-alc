import sys
input=sys.stdin.readline
n=int(input())
p=[0]*101
p[0]=0
p[1]=1
p[2]=1
p[3]=1
for i in range (3,101):
    p[i]=p[i-3]+p[i-2]
for i in range(n):
    a=int(input())
    print(p[a])