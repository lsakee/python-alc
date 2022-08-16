
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
arrs=[]
for _ in range(n):
    i1,i2=map(int,input().split())
    arrs.append((i1,i2))
dp = [0] * (m+1)
for arr in arrs:
    i1,i2=arr
    for i in range(m,i1-1, -1):
        if i < i1:
            dp[i] = dp[i-1]
        else:
             dp[i] = max(dp[i],dp[i-i1]+i2)
print(dp[-1])
