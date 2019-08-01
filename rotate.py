import math
import os
import random
import re
import sys

ar = [1,2,3,4,5]


def ans(arr, rot):
    arLen = len(ar)
    ans = [None] * arLen
    for i in range (arLen):
        indx = (arLen + i - rot) % arLen
        print(indx)
        if ( indx < 0 ):
            indx += arLen
        ans[indx] = arr[i]
    print(ans)
    return ans

ans(ar, 3)