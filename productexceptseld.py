def alg(nums):
    left = []
    right = []
    left.append(nums[0])
    right.append(nums[-1])
    for i in range(1,len(nums)):
        left.append(nums[i] * left[i-1])
    for j in range(len(nums) - 2, -1, -1):
        right.append(nums[j] * right[len(nums) - j - 2])
    nums[0] = right[-2]
    nums[len(nums) - 1] = left[len(nums) - 2]
    for i in range(1,len(nums)-1):
        nums[i] = left[i - 1] * right[ len(nums) - i - 2 ]

    return nums, left, right

print(alg([1,2,3,4]))