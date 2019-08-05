def getPath(node):
    if node == None:
        return None
    val = node.val
    left = getPath(node.left)
    right = getPath(node.right)
    if right == None:
        right = val
    elif left == None:
        left = val
    else:
        left = map(lambda x: val + "->" + x, left)
        right = map(lambda x: val + "->" + x, right)
    return left + right
        
def tree(root):
    if root == None:
        return []
    val = str(root.val)
    if root.left:
        left = map(lambda x: val + "->" + x, getPath(root.left))
    if root.right:
        right = map(lambda x: val + "->" + x, getPath(root.right))
    return left + right

