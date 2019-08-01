from typing import Dict, List
def maxArea(height: List[int]) -> int:
    i = 0
    j = len(height) - 1
    vol = 0
    while i != j:
        l = j - i
        v = l * min(height[i], height[j])
        vol = max(vol, v)
        if height[i] < height[j]:
            i += 1
        else: j -= 1
    return vol

maxArea([1,8,6,2,5,4,8,3,7])