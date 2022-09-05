import sys
input=sys.stdin.readline
a = int(input())
b = 0

while a >= 0:
    if a % 5 == 0:		# 남은 설탕이 5로 나누어 떨어진다면
        b += a // 5	# 봉지 개수를 더하고 끝
        print(b)
        break
    a -= 3			# 아니라면 3kg짜리 봉지를 하나씩 더해본다
    b += 1
else:
    print(-1)			# 빼다가 총 설탕이 음수가 되면 -1

