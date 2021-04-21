# Python3 递归
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def postorder(root: TreeNode):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        res = []
        postorder(root)

        return res

# Python3 迭代
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root == None:
            return res

        stk = []
        prev = None # 用于标记右子树是否已经遍历过

        while root or stk:
            while root:
                stk.append(root)
                root = root.left
            
            root = stk.pop()
            if root.right == None or root.right == prev: # 无右子树的节点 或者 右子树已遍历的非叶子节点
                res.append(root.val)
                prev = root
                root = None
            else:   # 右子树未遍历的非叶子节点
                stk.append(root)
                root = root.right
        
        return res


