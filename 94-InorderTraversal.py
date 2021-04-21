# Python3 递归 时间复杂度：O(n) 空间复杂度：O(n)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder(root, res):
            if root == None:
                return
            
            inorder(root.left, res)
            res.append(root.val)
            inorder(root.right, res)
        
        res = []
        inorder(root, res)
        return res

# C++ 递归
class Solution {
public:
    void inorder(TreeNode* root, vector<int>& res) {
        if (!root) { // 遇到空节点返回
            return;
        }

        inorder(root->left, res);
        res.push_back(root->val);
        inorder(root->right, res);
    }

    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        inorder(root, res);

        return res;
    }
};

# Java 递归
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        inorder(root, res);
        return res;
    }

    public void inorder(TreeNode root, list<Integer> res) {
        if (root == null) {
            return;
        }

        inorder(root.left, res);
        res.add(root.val);
        inorder(root.right, res);
    }
}

# Python3 迭代
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stk = []

        while root != None or stk != []:
            while root != None:
                stk.append(root)
                root = root.left
            root = stk[-1]
            stk.pop()
            res.append(root.val)
            root = root.right

        return res            

# C++ 迭代
# 递归与迭代两种方式是等价的，区别在于递归隐式地维护了一个栈，
# 迭代需要显示模拟这个栈
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode * right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> stk;

        while (root != nullptr || !stk.empty()) {
            while (root != nullptr) {
                stk.push(root);
                root = root->left;
            }

            root = stk.top();
            stk.pop();
            res.push_back(root->val);
            root = root->right;
        }
        return res;
    }
};