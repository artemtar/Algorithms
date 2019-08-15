def contains(nums, k, t):
    if k < 0 or t <= 0:
        return False
    if t == 1:
        for i in range(1, len(nums)):
            if abs(nums[i] - nums[i -1]) <= t:
                return True
    bucket = {}
    start = False
    count = 0
    for i in range(k, len(nums)):
        if count => t:
            start = True
        if k == 0:
            bk = nums[i]
        else:
            bk = nums[i] // k
        if bk in bucket:
            return True
        if k > 0 and (bk + 1 in bucket or bk - 1 in bucket):
            return True
        bucket[bk] = 1
        if start:
            if k == 0:
                del bucket[nums[i - t]]
            else:
                del bucket[nums[i - t] // k]
        count += 1

    return False
