from cgi import print_arguments
import sys
input=sys.stdin.readline
N=int(input())
list=[]
for i in range(N):
    T=int(input())
    list.append((T))
list.sort()
for i in range(N):
    print(list[i])    