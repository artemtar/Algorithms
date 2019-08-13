from collections import Counter
def findAna(s, p):
    sizeP = len(p)
    sizeS = len(s)
    if sizeS < sizeP:
        return []
    pDic = Counter(p)
    answer = []
    pDicCopy = pDic.copy()
    for i in range(0, sizeS - sizeP + 1):
        if s[i] not in pDic:
            continue
        if s[i + sizeP - 1] not in pDic:
            continue
        pDicCopy[s[i]] -= 1
        for j in range (i + 1, sizeP + i):
            if j >= sizeS:
                return answer
            if s[j] not in pDic:
                i = j + 1
                pDicCopy = pDic.copy()
                break
            else:
                pDicCopy[s[j]] -= 1
        flag = True
        for e in pDicCopy.values():
            if e != 0:
                flag = False
                break
        if flag:
            answer.append(i)

        pDicCopy = pDic.copy()
    return answer

print(findAna("abacbabc","abc"))
                
