# Python3
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

# 递归 对称二叉树的后序遍历和“逆后序遍历”所得结果应该相同，遍历至空节点插入None用于标识
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def leftTraverse(root: TreeNode):
            if not root:
                leftList.append(None)
                return
            leftTraverse(root.left)
            leftTraverse(root.right)
            leftList.append(root.val)

        def rightTraverse(root: TreeNode):
            if not root:
                rightList.append(None)
                return
            rightTraverse(root.right)
            rightTraverse(root.left)
            rightList.append(root.val)
        
        leftList = list()
        rightList = list()
        leftTraverse(root)
        rightTraverse(root)

        while len(leftList):
            if leftList.pop() != rightList.pop():
                return False
        
        return True

# 迭代 层序遍历，然后检查每一层是否为回文数组
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root]
        
        while(queue):
            next_queue = list()
            layer = list()
            for node in queue:
                if not node:
                    layer.append(None)
                    continue
                next_queue.append(node.left)
                next_queue.append(node.right)
                
                layer.append(node.val)
                
            if layer != layer[::-1]:
                return False
            queue = next_queue
            
        return True

# 递归
# 两个树互为镜像：
# 它们的两个根结点具有相同的值
# 每个树的右子树都与另一个树的左子树镜像对称
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            
            if node1.val != node2.val:
                return False
            
            return check(node1.left, node2.right) and check(node1.right, node2.left)
        
        return check(root, root)

# 实现这样一个递归函数，通过「同步移动」两个指针的方法来遍历这棵树，
# p 指针和 q 指针一开始都指向这棵树的根，随后 p 右移时，q 左移，p 左移时，q 右移。
# 每次检查当前 p 和 q 节点的值是否相等，如果相等再判断左右子树是否对称。
# 时间复杂度：这里遍历了这棵树，渐进时间复杂度为 O(n)。
# 空间复杂度：这里的空间复杂度和递归使用的栈空间有关，这里递归层数不超过 n，故渐进空间复杂度为O(n)。

# C++
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    bool check(TreeNode *p, TreeNode *q) {
        if (!p && !q) return true;
        if (!p || !q) return false;
        return p->val == q->val && check(p->left, q->right) && check(p->right, q->left);
    }

    bool isSymmetric(TreeNode* root) {
        return check(root, root);
    }
};
