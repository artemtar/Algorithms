def _helper(node):
    node.left.val, node.right.val = node.right.val, node.left.val 
def invertTree(root):
    if not root:
        return
    else:
        left = root.left
        right = root.right
    