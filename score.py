def climbingLeaderboard(scores, alice):
    # scoreDic = {e:0 for e in set(scores)}
    # for e in scores:
    #     scoreDic[e] += 1
    newScores = sorted(list(set(scores)), reverse=True)
    aliceRank = []
    for al in alice:
        rank = 1
        for e in newScores:
            if e > al:
                rank += 1
            else: break
        aliceRank.append(rank)
    return aliceRank

a = [100, 100, 50, 40, 40, 20, 10,]
b = [5, 25, 50, 120]

rank = climbingLeaderboard(a, b)
print(rank)