# Python3
class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 终止条件：树为空时结束递归，返回当前深度0
        if root == None:
            return 0
        
        # root的左右子树的最大深度
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        # 返回值为左右子树的最大深度+1
        return max(leftDepth, rightDepth) + 1

# 递归解题三部曲模版： https://lyl0724.github.io/2020/01/25/1/
# 1.找终止条件。 
# 什么情况下递归结束？当然是树为空的时候，此时树的深度为0，递归就结束了。
# 2.找返回值。 
# 应该返回什么？题目求的是树的最大深度，需要从每一级得到的信息自然是当前这一级对应的树的最大深度，
# 因此返回值应该是当前树的最大深度，这一步可以结合第三步来看。
# 3.本级递归应该做什么。 
# 首先，还是强调要走出之前的思维误区。
# 此时就考虑递归每一级的三个节点：root、root.left、root.right，
# 其中根据第二步，root.left和root.right分别记录的是root的左右子树的最大深度。
# 那么本级递归应该做什么就很明确了，自然就是在root的左右子树中选择较大的一个，
# 再加上1就是以root为根的子树的最大深度了，然后再返回这个深度即可。

# DFS 递归
# 时间复杂度：O(n)，其中 n 为二叉树节点的个数。每个节点在递归中只被遍历一次。
# 空间复杂度：O(height)，其中 height 表示二叉树的高度。
# 递归函数需要栈空间，而栈空间取决于递归的深度，因此空间复杂度等价于二叉树的高度。
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return 0 if root == None else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# BFS 
# 广度优先搜索的队列里存放的是「当前层的所有节点」。
# 每次拓展下一层的时候，不同于广度优先搜索的每次只从队列里拿出一个节点，
# 需要将队列里的所有节点都拿出来进行拓展，这样能保证每次拓展完的时候队列里存放的是当前层的所有节点，
# 即一层一层地进行拓展，最后用一个变量 ans 来维护拓展的次数，该二叉树的最大深度即为 ans。

# 时间复杂度：O(n)，其中 n 为二叉树的节点个数。与方法一同样的分析，每个节点只会被访问一次。
# 空间复杂度：此方法空间的消耗取决于队列存储的元素数量，其在最坏情况下会达到 O(n)。
# Python3
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = list()
        ans = 0
        queue.append(root)

        while len(queue):
            cnt = len(queue)
            while cnt:
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cnt -= 1
            ans += 1
        
        return ans

# C++
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }

        queue<TreeNode*> Q;
        Q.push(root);

        int ans = 0;
        while (!Q.empty()) {
            int sz = Q.size();
            while (sz > 0) {
                TreeNode* node = Q.front();
                Q.pop();

                if (node->left) {
                    Q.push(node->left);
                }
                if (node->right) {
                    Q.push(node->right);
                }

                sz -= 1;
            }
            ans += 1;
        }
    }
};

# Java
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.offer(root);

        int ans = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            while (size > 0) {
                TreeNode node = queue.poll();
                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
                size--;
            }
            ans++;
        }
        return ans;
    }
}