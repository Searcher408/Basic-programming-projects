# Python3
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

# DFS
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        elif not root2:
            return root1

        root1.val += root2.val
        # left = self.mergeTrees(root1.left, root2.left)
        # right = self.mergeTrees(root1.right, root2.right)
        # root1.left = left
        # root1.right = right
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1

# BFS
# 时间复杂度：O(min(m,n))，其中 m 和 nn 分别是两个二叉树的节点个数。
# 对两个二叉树同时进行广度优先搜索，只有当两个二叉树中的对应节点都不为空时才会访问到该节点，
# 因此被访问到的节点数不会超过较小的二叉树的节点数。
# 空间复杂度：O(min(m,n))，空间复杂度取决于队列中的元素个数，
# 队列中的元素个数不会超过较小的二叉树的节点数。
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        
        merged = TreeNode(t1.val + t2.val)
        queue = collections.deque([merged])
        queue1 = collections.deque([t1])
        queue2 = collections.deque([t2])

        while queue1 and queue2:
            node = queue.popleft()
            node1 = queue1.popleft()
            node2 = queue2.popleft()

            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right

            if left1 or left2:
                if left1 and left2:
                    left = TreeNode(left1.val + left2.val)
                    node.left = left
                    queue.append(left)
                    queue1.append(left1)
                    queue2.append(left2)
                elif left1:
                    node.left = left1
                elif left2:
                    node.left = left2
            
            if right1 or right2:
                if right1 and right2:
                    right = TreeNode(right1.val + right2.val)
                    node.right = right
                    queue.append(right)
                    queue1.append(right1)
                    queue2.append(right2)
                elif right1:
                    node.right = right1
                elif right2:
                    node.right = right2
            
        return merged