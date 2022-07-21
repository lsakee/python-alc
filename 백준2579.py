
import itertools
n = int(input())
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
num = list(itertools.permutations(nums, 3))
#itertools.permutations 은 순열 파이썬 문법을 몰라 검색후 확인했음 
#순열 기능을 알면 금방 해결하는 문제인거 같다


count = 0
for _ in range(n):
    n, s, b = map(int, input().split())
    n = list(str(n))  # int는 리스트가 될 수 없다
    count = 0
    for i in range(len(num)):
        str = 0
        ball = 0
        i -= count  
        # num[0]부터 찾아야함
        for j in range(3):
            if num[i][j] == n[j]: 
                # 입력한 숫자를 한칸 씩 지니가며 숫자야구 시작숫자(한자리) 적중하면 올리기
                str += 1
            elif n[j] in num[i]: 
                # 입력한 숫자(한자리)가 num안에 들어있으면 ball ++
                ball += 1

        if (str != s) or (ball != b): 
            ##입력 받은 수가 없으면 후보 삭제
            num.remove(num[i])
            count += 1

print(len(num))