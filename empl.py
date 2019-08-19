def getImp(employees, idx):
    empDict = {emp.id: emp for emp in employees}
    stack = [idx]
    seen = []
    imp = 0
    while stack:
        nextId = stack.pop()
        if nextId not in seen:
            seen.append(nextId)
            nextEmp = empDict[nextId]
            imp += nextEmp.importance
            stack.extend(nextEmp.subordinates)
    return imp
        