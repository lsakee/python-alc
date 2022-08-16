import sys
input=sys.stdin.readline
n = int(input()) 
d=[1,2]
if (n>=3) :
    for i in range(2,n) :
    #그전 코드는 어펜드가아님 sum이용했음
        d.append(d[i-2]+d[i-1])
    print(d[i]%10007)
else :
    print(n)
