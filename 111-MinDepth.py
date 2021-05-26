# Python3
import collections
from typing import Collection


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
         
        if not root.left and not root.right: # 左右子树都为空
            return 1
        
        if not root.left: # 左子树为空但右子树不为空
            return self.minDepth(root.right) + 1
        elif not root.right: # 右子树为空但左子树为空
            return self.minDepth(root.left) + 1
        else: # 左右子树都不为空
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

# BFS
# 当找到一个叶子节点时，直接返回这个叶子节点的深度。广度优先搜索的性质保证了最先搜索到的叶子节点的深度一定最小。
# 时间复杂度：O(N)，其中 N 是树的节点数。对每个节点访问一次。
# 空间复杂度：O(N)，其中 N 是树的节点数。空间复杂度主要取决于队列的开销，队列中的元素个数不会超过树的节点数。
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = collections.deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth
            
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        
        return 0
