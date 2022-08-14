import sys
input=sys.stdin.readline
n = int(input())
lists=[]
for _ in range(n):
    lists.append(input().strip())
    #계속해도 안돼서 .strip 추가
words=set(lists)
lists=list(words)
lists.sort()
lists.sort(key=len)
for i in range(len(lists)):
    print(lists[i])