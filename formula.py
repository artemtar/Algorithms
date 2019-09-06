def countAtoms(formula):
    if "(" not in formula:
        ans = {}
        for i in len(formula):
            value = None
            try:
                value = int(formula[i])
            except:
                value = formula[i]
            if type(value) == 'int':
                ans[i - 1] = ans[i - 1] * value
            else:
                if i == len(formula) - 1:
                    ans[]

    else:
        firstB = 0
        for i in len(formula):
            if formula[i] == "(":
                firstB = i
                break
            else:

        i = 1
        nextB = i
        while i < len(formula):
            if formula[i] == ")":
                nextB = i
        recCall = countAtoms(formula[firstB + 1:nextB])
            