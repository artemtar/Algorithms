from typing import Dict, List
def isPossible(nums: List[int]) -> bool:
    if len(nums) < 3: return False
    count = 0
    for e in range(1, len(nums)):
        if nums[e] != nums[e-1] + 1:
            if count < 2:
                return False
            count = 0
        
    if count < 2: return False
    else: return True

print(isPossible([1,2,3,3,4,5]))