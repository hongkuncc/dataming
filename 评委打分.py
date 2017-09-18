pScore=[9,9,10,8,9,8.5,8,10,7,8]
gScore=9
pScore.sort()
pScore.pop()
pScore.pop(0)
pScore.append(gScore)
aveScore=sum(pScore)/len(pScore)
print aveScore

