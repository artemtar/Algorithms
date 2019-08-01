def find_top(ma, bot, top, last):
    mid = (top - bot) // 2 + bot
    if mid == 0:
        return 0
    elif mid == last:
        return last
    else:
        left = ma[(mid - 1)]
        right = ma[(mid + 1)]
        midp = ma[mid]
        if (midp >= left and midp >= right):
            return mid
        if (midp >= left and midp < right):
            return find_top(ma, mid, top, last)
        else: return find_top(ma, bot, mid, last)
        
def search_left(target, ma, bot, top):
    if bot == top:
        return -1
    mid = bot + (top - bot) // 2
    midp = ma[mid]
    if midp == target:
        return mid
    if (bot + 1) == top:
        if ma[top] == target:
            return top
        elif ma[bot] == target:
            return bot
        else: return -1
    elif midp < target:
        return search_left(target, ma, mid, top)
    else: return search_left(target, ma, bot, mid)
    
def search_right(target, ma, peack, bottom):
    if peack == bottom:
        return -1
    mid = peack + (bottom - peack) // 2
    midp = ma[mid]
    if midp == target:
        return mid
    if (peack + 1) == bottom:
        if ma[bottom] == target:
            return bottom
        elif ma[peack] == target:
            return peack
        else: return -1
    if target < midp:
        return search_right(target, ma, midp, bottom)
    return search_right(target, ma, peack, midp)

def findInMountainArray(target: int, mountain_arr):
            mLen = len(mountain_arr)
            top_ind = find_top(mountain_arr, 0, mLen - 1, mLen - 1)
            ind = search_left(target, mountain_arr, 0, top_ind)
            if ind == -1:
                ind = search_right(target, mountain_arr, top_ind, mLen - 1)
            return ind





print(findInMountainArray(3, [0,1,2,4,2,1]))