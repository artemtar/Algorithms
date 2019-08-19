def sumarray(nums):
    nums = sorted(nums)
    toRet = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            toRet += nums[i]
    return toRet