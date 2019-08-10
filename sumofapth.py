class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def helper(root, sums, cur):
    if not root.left and not root.right:
        if sums == cur + root.val:
            return [[root.val]]
        else: return None
    else:
        left = root.left
        right = root.right
        val = root.val
        leftRet = None
        rightRet = None
        if left:
            if val + left.val + cur <= sums:
                leftRet = helper(root.left, sums, val + cur)
                if leftRet:
                    leftRet = list(map(lambda x: [val] + x, leftRet))
        if right:
            if val + right.val + cur <= sums:
                rightRet = helper(root.right, sums, val + cur)
                if rightRet:
                    rightRet = list(map(lambda x: [val] + x, rightRet))
        
        if not leftRet and not rightRet:
            return None
        elif not leftRet:
            return rightRet
        elif not rightRet:
            return leftRet
        else: return rightRet + leftRet


def pathSum(root, sums):
    if not root:
        return None
    else:
        return helper(root, sums, 0)


root = TreeNode(1)
root.left = TreeNode(-2)
root.right = TreeNode(-3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(-2)
root.left.left.left = TreeNode(-1)
print(pathSum(root, -1))