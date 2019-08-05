def findDuplicate(nums):
    for i in range(len(nums)):
        elem = nums[i]
        if elem != i:
            while(elem != i):
                temp = elem
                elem = nums[temp]
                if temp == elem:
                    return temp
                nums[temp] = temp
            nums[i] = elem
    return -1

print(findDuplicate([3,1,3,4,2]))