# Python3
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right= right

# 后序遍历
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        if not root.left and not root.right:
            return root
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # tmp = root.left
        # root.left = root.right
        # root.right = tmp
        root.left, root.right = root.right, root.left

        return root
    
# Java
class Solution {
    // 先序遍历，从顶向下交换
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;

        // 保存右子树
        TreeNode rightTree = root.right;

        // 交换左右子树的位置
        root.right = invertTree(root.left);
        root.left = invertTree(rightTree);
        return root;
    }
}

class Solution {
    // 中序遍历
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;
        invertTree(root.left); // 递归找到左节点
        TreeNode rightNode = root.right; // 保存右节点
        root.right = root.left;
        root.left = rightNode;

        // 递归找到右节点继续交换
        // 因为此时左右节点已交换，所以此时右节点为root.left
        invertTree(root.left);

        return root;
    }
}

class Solution {
    // 层次遍历，直接左右交换即可
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            TreeNode rightTree = node.right;
            node.right = node.left;
            node.left = rightTree;

            if (node.left != null) {
                queue.offer(node.left);
            }
            if (node.right != null) {
                queue.offer(node.right);
            }
        }

        return root;
    }
}