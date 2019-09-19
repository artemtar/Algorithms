def hap(n):
    dic = {}
    sums = 0
    q = [n]
    while q:
        nn = q.pop()
        if nn in dic:
            return False
        dic[nn] = 1
        rem = 0
        sumnum = 0
        while nn != 0:
            rem = nn % 10
            nn = nn // 10
            sums += rem ** 2
        sums += sumnum
        if sums == 1:
            return True
        sumnum = 0
        q.append(sums)
        sums = 0
    return False

def helper(num):
    numSum = 0
    rem = 0
    while num != 0:
        rem = num % 10
        num = num // 10
        numSum += rem ** 2
    return numSum
def hapcycl(n):
    slow = lambda x : helper(x)
    fast = lambda x : helper(helper(x))
    slowNum = slow(n)
    fastNum = fast(n)
    if fastNum == 1:
        return True
    while slowNum != fastNum:
        slowNum = slow(slowNum)
        fastNum = fast(fastNum)
        if fastNum == 1:
            return True
    return False

print(hapcycl(19))