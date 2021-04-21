# Python3 
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]: 
        ret = [] # 二维列表
        if root == None:
            return ret
        q = [] # 队列，列表模拟
        q.append(root)

        while q != []:
            n = len(q)
            tmp = []

            for _ in range(n):
                node = q[0] 
                tmp.append(node.val)    

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                q.pop(0) # 删除队列头部元素

            ret.append(tmp)

        return ret

# C++ 广度优先搜索
# 时间复杂度：每个点进队出队各一次，故渐进时间复杂度为 O(n)
# 空间复杂度：队列中元素的个数不超过 nn 个，故渐进空间复杂度为 O(n)
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ret;
        if (!root) {
            return ret;
        }

        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            int currentLevelSize = q.size();
            ret.push_back(vector<int>());

            for (int i = 1; i <= currentLevelSize; i++) {
                auto node = q.front(); q.pop();
                ret.back().push_back(node->val); # ret.back() 取出每次 while 循环创建的新 vector

                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
        }

        return ret;
    }
};

# C++队列 Queue 类成员函数如下:
# back() 返回最后一个元素
# empty() 如果队列空则返回真
# front() 返回第一个元素
# pop() 删除第一个元素
# push() 在末尾加入一个元素
# size() 返回队列中元素的个数