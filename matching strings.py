import math
import os
import random
import re
import sys

s = ['def', 'de', 'fgh']
q = ['de', 'lmn', 'fgh']

def matchingStrings(strings, queries):
    lenQ = len(q)
    sSorted = sorted(strings)
    qSorted = sorted(queries)
    asnDictionary = {e:0 for e in queries}
    k = 0
    flag = False
    for i in range(lenQ):
        if sSorted[k] < qSorted[i]:
            while(sSorted[k] < qSorted[i]):
                k += 1
                if k > len(sSorted) - 1:
                    flag = True
                    break
        if flag:
            break
        if sSorted[k] == qSorted[i]:
            while(sSorted[k] == qSorted[i]):
                asnDictionary[qSorted[i]] += 1
                k += 1
                if k > len(sSorted) - 1:
                    flag = True
                    break
        if flag:
            break
    toReturn = []
    for e in queries:
        toReturn.append(asnDictionary[e])
    print(toReturn)
matchingStrings(s, q)

def staircase(n):
    for i in range(n, 0, -1):
        stars = n - i
        while stars > 0:
            print("", end = " ")
            stars -= 1
        for _ in range(i):
            print("#", end="")
        print("")

staircase(6)