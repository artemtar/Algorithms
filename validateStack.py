def validate(pushed, popped):
    if not pushed and not popped:
        return True
    if len(pushed) != len(popped):
        return False
    stack = []
    while pushed:
        e = pushed.pop(0)
        if e == popped[0]:
            popped.pop(0)
            while stack and popped:
                if stack[-1] == popped[0]:
                    stack.pop()
                    popped.pop(0)
                else:
                    break
        else:
            stack.append(e)
    while stack and popped:
        if stack.pop(0) != popped.pop():
            return False
    if not stack:
        return True
    else: return False
        


print(validate([1,2,3,4,5], [4,3,5,1,2]))