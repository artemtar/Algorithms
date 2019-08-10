class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def getPath(node):
        if not node:
            return [[]]
        elif not node.left and not node.right:
            return [[node.val]]
        else:
            left = []
            right = []
            if node.left:
                left = getPath(node.left)
                left = list(map(lambda x: [node.val] + x, left))
            if node.right:
                right = getPath(node.right)
                right = list(map(lambda x: [node.val] + x, right))
            return left + right

def binaryTreePaths(root):
    if not root:
        return []
    else:
        paths = getPath(root)
        paths = list(map(lambda x: [str(y) for y in x], paths))
        paths = list(map(lambda x: "->".join(x), paths)) 
        return paths

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

print(binaryTreePaths(root))