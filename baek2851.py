super = []
score = 0
for i in range(10):
    super.append(int(input()))
for k in super:
    bscore = score
    score = score+k
    if score >= 100:
        if score - 100 > 100 - bscore:
            score = bscore
        break
print(score)