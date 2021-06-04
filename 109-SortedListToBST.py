# Python3
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 根据中位数的性质，链表中小于中位数的元素个数与大于中位数的元素个数要么相等，要么相差 1。
# 使用分治的思想，继续递归地对左右子树进行构造，找出对应的中位数作为根节点。

# 分治 时间复杂度：O(nlogn)，其中 n 是链表的长度。空间复杂度：O(logn)，为递归过程中栈的最大深度。
# 当前链表的左端点为left，右端点right，包含关系为「左闭右开」，即left 包含在链表中而right 不包含在链表中。
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getMedian(left: ListNode, right: ListNode) -> ListNode:
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def buildTree(left: ListNode, right: ListNode) -> TreeNode:
            if left == right:
                return None
            mid = getMedian(left, right)
            root = TreeNode(mid.val)
            root.left = buildTree(left, mid)
            root.right = buildTree(mid.next, right)
            return root
        
        return buildTree(head, None)

# 分治 + 中序遍历优化
# 方法一的时间复杂度的瓶颈在于寻找中位数节点。
# 由于构造出的二叉搜索树的中序遍历结果就是链表本身，因此可以将分治和中序遍历结合起来，减少时间复杂度。
# 当前链表的左端点编号为 left，右端点编号为 right，包含关系为「双闭」，即 left 和 right 均包含在链表中。
# 时间复杂度：O(n)，其中 n 是链表的长度。空间复杂度：O(logn)
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getLength(head: ListNode) -> int:
            ret = 0
            while head:
                ret += 1
                head = head.next
            return ret
        
        def buildTree(left: int, right: int) -> TreeNode:
            if left > right:
                return None
            
            mid = (left + right + 1) // 2
            root = TreeNode()
            root.left = buildTree(left, mid - 1)
            nonlocal head
            root.val = head.val
            head = head.next
            root.right = buildTree(mid + 1, right)
            return root
        
        length = getLength(head)
        return buildTree(0, length - 1)

# global和nonlocal的作用都是可以实现代码块内变量使用外部的同名变量
# global很明显就是声明代码块中的变量使用外部全局的同名变量
# nolocal 的使用场景就比较单一，它是使用在闭包中的，使变量使用外层的同名变量

# /**
#  * Definition for singly-linked list.
#  * struct ListNode {
#  *     int val;
#  *     ListNode *next;
#  *     ListNode() : val(0), next(nullptr) {}
#  *     ListNode(int x) : val(x), next(nullptr) {}
#  *     ListNode(int x, ListNode *next) : val(x), next(next) {}
#  * };
#  */
# /**
#  * Definition for a binary tree node.
#  * struct TreeNode {
#  *     int val;
#  *     TreeNode *left;
#  *     TreeNode *right;
#  *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
#  *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
#  *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
#  * };
#  */

 # C++ bfs建树(完全二叉搜索树) + dfs填节点值
 # 完全二叉搜索树也是平衡二叉树
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        if (head == nullptr) {
            return nullptr;
        }

        ListNode* node = head;
        TreeNode* root= new TreeNode(0);
        queue<TreeNode*> que;
        que.push(root);
        node = node->next;
        while (node) {
            TreeNode* n = que.front();
            que.pop();
            n->left = new TreeNode(0);
            que.push(n->left);
            node = node->next;
            if (node == nullptr) {
                break;
            }
            n->right = new TreeNode(0);
            que.push(n->right);
            node = node->next;
        }
        dfsBuild(head, root);
        return root;
    }
private:
    void dfsBuild(ListNode*& node, TreeNode* root) {
        if (root == nullptr) {
            return;
        }
        dfsBuild(node, root->left);
        root->val = node->val;
        node = node->next;
        dfsBuild(node, root->right);
    }
};