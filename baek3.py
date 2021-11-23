n=int(input()) # 몇과목 #1546
test_list = list(map(int,input().split()))
max_score=max(test_list) # 최고점 과목 찾기
new_list=[]
for score in test_list:
    new_list.append(score/max_score *100)
test_avg =sum(new_list)/n # 새로운 값 저장후 평균 값 구하기
print(test_avg)