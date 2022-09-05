# import sys
# input=sys.stdin.readline
n=int(input())
f=[]
for i in range(n) :
     f.append(list(map(int, input().split())))

for i in range(1,n):
    for k in range(len(f[i])):
        if k==0:
            # f.append(f[i][k]+f[i-1][k])
            f[i][k] =(f[i][k]+f[i-1][k])
        elif i==k:
        #    f.append(f[i][k]+f[i-1][k-1])
           f[i][k] =(f[i][k]+f[i-1][k-1])
        else:
            # f.append(max(f[i - 1][k - 1], f[i - 1][k]) + f[i][k])
            f[i][k] = max(f[i - 1][k - 1], f[i - 1][k]) + f[i][k]
print(max(f[n-1]))
#       7                   1                  f[0][0]
#   10        15            2 f[0][0]+f[1][0]          f[0][0]+f[1][1]
# 18   11    16   15        4 f[0][0]+f[1][0]+f[2][0]       f[0][0]+f[1][1]+f[2][2]
#20 25 18 15 23 20  19  19   8