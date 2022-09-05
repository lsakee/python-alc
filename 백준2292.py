import sys
input=sys.stdin.readline
n = int(input())
f=1
c=1
while n>f:
    f=f+(6*c)
    c+=1
print(c)