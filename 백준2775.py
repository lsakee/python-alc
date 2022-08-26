import sys
input=sys.stdin.readline
n = int(input())

for _ in range(n):  
    a = int(input()) 
    b = int(input())  
    cnt = [i for i in range(1, b+1)]  
    for k in range(a):  
        for i in range(1, b): 
            cnt[i] += cnt[i-1]  
    print(cnt[-1])  
    
    # 1234
    # 13610
    #1410