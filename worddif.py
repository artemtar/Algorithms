def appendAndDelete(s, t, k):
    lens = len(s)
    lent = len(t)
    shortest = min(lens, lent)
    longest = max(lens, lent)
    count = shortest
    for i,j in zip(s, t):
        if i == j:
            count -= 1
        else:
            break
    num = shortest - longest + count
    if num <= k:
        return "yes"
    else: return "no"

appendAndDelete([1,2,3], [1,2], 2)