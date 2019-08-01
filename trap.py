from typing import Dict, List
def volL(l, r, height):
    if l == r or l == r -1:
        return 0
    if sum(height[l:r]) == 0:
        return 0
    mp = 0
    mh = 0
    for i in range(l, r):
        if height[i] > mp:
            mp = height[i]
            mh = i
    peble = sum(height[mh + 1:r])
    vol = (r - mh - 1) * min(mp, height[r]) - peble
    return vol + volL(0, mh, height)

def volR(l, r, height):
    if l == r or l == r - 1:
        return 0
    if sum(height[l + 1:]) == 0:
        return 0
    mp = 0
    mh = 0
    for i in range(l + 1, r):
        if height[i] >= mp:
            mp = height[i]
            mh = i
    peble = sum(height[l + 1:mh])
    vol = (mh - l - 1) * min(mp, height[l]) - peble
    return vol + volR(mh, r, height)

def trap(height: List[int]) -> int:
    if len(height) < 3:
        return 0
    max1 = 0
    max2 = 0
    m1 = 0
    m2 = 0
    for i in range(len(height)):
        e = height[i]
        if e > m1:
            m2 = m1
            m1 = e
            max2 = max1
            max1 = i 
        elif e >= m2:
            m2 = e
            max2 = i
    l = min(max1, max2)
    r = max(max1, max2)
    if l >= r - 1:
        vm = 0
    else:
        peble = 0
        for i in range(l + 1, r):
            peble += height[i]
        vm = min(m1, m2) * (r - l - 1) - peble
    vl = volL(0, l, height)
    vr = volR(r, len(height), height)
    return vm + vl + vr


print(trap([5,4,1,2]))