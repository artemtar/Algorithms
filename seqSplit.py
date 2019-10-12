from collections import Counter
def isPossible(nums):
    c = Counter(nums)
    for i in nums:
        while c[i] != 0:
            c[i] -= 1
            y = i + 1
            while c[y] > 0 and c[y]:
                c[y] -= 1
                if c[y] >= c[y + 1]:
                    break
                y += 1
        if y - i < 3:
            return False
    return True
            


print(isPossible([1,2,3,3,4,4,5,5]))