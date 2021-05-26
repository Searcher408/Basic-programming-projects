# Python3
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

# 定义一个ReturnNode类用作返回值
# 一棵树是BST等价于它的左、右子树都是BST且子树高度差不超过1
# 返回值应该包含当前树是否是BST和当前树的高度这两个信息
class ReturnNode:
    def __init__(self, isBalanced: bool, depth: int) -> None:
        self.isBalanced = isBalanced
        self.depth = depth

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBST(root).isBalanced

    def isBST(self, root: TreeNode) -> ReturnNode:
        if root == None: # 子树为空的时候，空树自然是平衡二叉树，递归终止
            return ReturnNode(True, 0)
        
        # 不平衡的情况有3种：左树不平衡、右树不平衡、左树和右树差的绝对值大于1
        left = self.isBST(root.left)
        right = self.isBST(root.right)
        if left.isBalanced == False or right.isBalanced == False:
            return ReturnNode(False, 0)
        if abs(left.depth - right.depth) > 1:
            return ReturnNode(True, 0)
        
        # 不满足上面3种情况，说明平衡了，树的深度为左右俩子树最大深度+1
        return ReturnNode(max(left.depth, right.depth)+1, True)

# 自顶向下的递归
# 时间复杂度：O(n^2), 其中 n 是二叉树中的节点个数
# 空间复杂度：O(n)，空间复杂度主要取决于递归调用的层数，递归调用的层数不会超过 n。
# 自顶向下递归类似于二叉树的前序遍历，即对于当前遍历到的节点，首先计算左右子树的高度，
# 如果左右子树的高度差是否不超过 1，再分别递归地遍历左右子节点，并判断左子树和右子树是否平衡。
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1
        
        if not root:
            return True
        
        return abs(height(root.left) - height(root.right)) <= 1 \
                and self.isBalanced(root.left) and self.isBalanced(root.right)

# 主要的代码换行有通用的反斜杠\和针对字符串起作用的三引号结构。

# 自底向上的递归 时间复杂度O(n), 空间复杂度O(n)
# 自顶向下递归对于同一个节点，函数 height 会被重复调用，导致时间复杂度较高。
# 如果使用自底向上的做法，则对于每个节点，函数 height 只会被调用一次。
# 自底向上递归的做法类似于后序遍历，对于当前遍历到的节点，先递归地判断其左右子树是否平衡，
# 再判断以当前节点为根的子树是否平衡。如果一棵子树是平衡的，则返回其高度（高度一定是非负整数），
# 否则返回 -1。如果存在一棵子树不平衡，则整个二叉树一定不平衡。
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1
            
        return height(root) >= 0

      