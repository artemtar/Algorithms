def search(idx, emp, low, high):
    if low == high:
        return -1
    mid = (high - low) // 2
    if emp[mid] = idx:
        return mid
    else:
        if emp[mid] < idx:
            return search(idx, emp, mid, high)
        else: return search(idx, emp, low, mid)
    
def getImp(employees, id):
    employees.sort(lambda x: x.id, reversed = False)
    seen = []
    toVisit = [id]
    ans = 0
    while toVisit:
        nextId = toVisit.pop(0)
        if nextId in seen:
            continue
        else:
            seen.append(nextId)
