
import sys
input=sys.stdin.readline
n = int(input())
num = map(int, input().split())
result = 0
for i in num:
    count = 0
    if i > 1 :
#그전까자만 시작은 2부터소수
        for j in range(2, i):  
            if i % j == 0:
# 소수는 자기자신만으로 나눠짐 근데 다른걸로 나눠지면 안됒
                count += 1  
        if count == 0:
            result += 1  # error가 없으면 소수.
print(result)