from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def find_target(root: TreeNode, k: int) -> bool:
    if not root: return False
    dic = {}
    dq = deque([root])
    while dq:
        node = dq.popleft()
        if k - node.val in dic: return True
        dic[node.val] = 1
        if node.left: dq.append(node.left)
        if node.right: dq.append(node.right)
    return False
