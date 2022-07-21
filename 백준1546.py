n = int(input())
N = list(map(int, input().split()))
max = max(N)

result = []
for i in N :
  j=i/max*100
  result.append(j)
lastresult = sum(result)/n
print(lastresult)