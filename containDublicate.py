def contains(nums):
    dict = {}
    for e in nums:
        if e not in nums:
            dict[e] = 0
        else:
            return False
    return True