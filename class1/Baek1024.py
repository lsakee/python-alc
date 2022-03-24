import random
super= []
score = 0
for i in range(10): 
    n = random.randrange(1,100)
    super.append(n)
    print(super[i])
for k in super:
    bscore = score
    score = score+k
    if score >= 100:
        if score - 100 > 100 - bscore:
            score = bscore
        break
print(score)
