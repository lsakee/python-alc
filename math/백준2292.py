import sys
input=sys.stdin.readline
n = int(input())
f=0
c=1
while n>f:
    c+=1
    i=1
    f=f+(i*6)
    f+=6
    i+=1
print(c)