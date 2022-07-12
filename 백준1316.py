
import sys
input=sys.stdin.readline
#입력을 받음d
n=int(input())
result=n
for i in range(n):
    gw = input()
    gw_len=len(str(gw))-1
    for j in range(0,gw_len):
        if gw[j] == gw[j+1]:
            pass
        elif gw[j] in gw[j+1:]:
            result -= 1
            break

print(result)