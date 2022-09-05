import sys
input=sys.stdin.readline
while True:
    n = input()
    if n=="0":
        break
    q="no"
    if n == n[::-1]:
        q="yes"
    print(q)
