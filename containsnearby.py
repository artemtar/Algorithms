def contains(nums, k):
    if k <= 0:
        return False
    bucket = {}
    for i in range(nums):
        if nums[i] in bucket:
            return True
        bucket[nums[i]] = 1
        if i >= k:
            del bucket[nums[i - k]]
    return False
