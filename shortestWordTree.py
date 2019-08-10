minval = 100000000 
minLen = 10000000

def helper(root, ls):
    if not root.left and not root.right:
        tempmin = sum(ls) + root.val
        global minval 
        global minLen
        if tempmin < minval and len(ls) + 1 <= minLen:
            minval = tempmin
            minLen = len(ls) + 1
            return [root.val], minLen
        else: return []
    left = None
    right = None
    if len(ls) + 1 < minLen and sum(ls) + root.val < minval:
        val = root.val
        if root.left and root.right:
            left = helper(root.left, ls + [val])
            right = helper(root.right, ls + [val])
        elif root.left:
            left = helper(root.left, ls + [val])
        elif root.right:
            right = helper(root.right, ls + [val])
        if left and right:
            if left[1] == right[1]:
                if sum(left[0]) < sum(right[0]):
                    return left[0] + [val], left[1]
                else: return right[0] + [val], right[1]
            if left[1] < right[1]:
                return left[0] + [val], left[1]
            else: return right[0] + [val], right[1]
        elif left:
            return left[0] + [val], left[1]
        elif right:
            return right[0] + [val], right[1]
        else: return []
    else: return []



def smalestFromLeaf(root):
    answer = helper(root, [])
    answer = list(map(lambda x: str(chr(x + 97)), answer[0]))
    answer = "".join(answer)
    return answer


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)

print(smalestFromLeaf(root))