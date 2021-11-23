word = input().lower() # 소문자로만#1157
word_list = list(set(word)) # 워드에 요소들만 
test =[]

for i in word_list:
    count=word.count(i)
    test.append(count)

if test.count(max(test)) >=2: #ex) 여러개가 있으면 머출력해?
    print("&") 
else:
    print(word_list[(test.index(max(test)))].upper())
