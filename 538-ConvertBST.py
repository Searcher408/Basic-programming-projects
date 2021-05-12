# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val = 0, left = None, right = None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     num = 0
    
#     def convertBST(self, root: TreeNode) -> TreeNode:  
#         self.unPreOrder(root)
#         return root
    
#     def unPreOrder(self, root: TreeNode) -> TreeNode:
#         if root == None:
#             return
#         self.unPreOrder(root.right)
#         root.val += self.num
#         self.num = root.val
#         self.unPreOrder(root.left)
#         return root

#     def convertBST_non_recursive(self, root: TreeNode) -> TreeNode:
#         # if root == None:
#         #     return root
        
#         num = 0
#         stk = []
#         node = root
#         while node != None or len(stk) != 0:
#             while node != None:
#                 stk.append(node)
#                 node = node.right
            
#             node = stk.pop()
#             node.val += num
#             num = node.val

#             if node.left != None:
#                 node = node.left
#             else:
#                 node = None
        
#         return root

# Java BST的中序遍历是从小到大顺序，反过来就是从大到小，依次累加即可
# class Solution {
#     int num = 0;

#     public TreeNode convertBST(TreeNode root) {
#         if (root != null) {
#             // 遍历右子树
#             convertBST(root.right);
#             // 遍历顶点
#             root.val = root.val + num;
#             num = root.val;
#             // 遍历左子树
#             convertBST(root.left);

#             return root;
#         }
#         return null;
#     }
# }

# Definition for a binary tree node.
# public class TreeNode {
#     int val;
#     TreeNode left;
#     TreeNode right;
#     TreeNode() {};
#     TreeNode(int val) { 
#         this.val = val; 
#     }
#     TreeNode(int val, TreeNode left, TreeNode right) {
#         this.val = val;
#         this.left = left;
#         this.right = right;
#     }
# }

# class Solution {
#     public int preNum = 0;

#     // 递归写法
#     /* public TreeNode convertBST(TreeNode root) {
#         unPreOrder(root);
#         return root;
#     }

#     public void unPreOrder(TreeNode root) {
#         if (root == null) {
#             return;
#         }
#         unPreOrder(root.right);
#         root.val += preNum;
#         preNum = root.val;
#         unPreOrder(root.left);
#     }*/

#     // 非递归写法
#     public TreeNode convertBST(TreeNode root) {
#         if (root == null) {
#             return root;
#         }

#         Stack<TreeNode> stack = new Stack<TreeNode>();
#         TreeNode node = root;
#         while (node != null || !stack.isEmpty()) {
#             while (node != null) {
#                 stack.add(node);
#                 node = node.right;
#             }

#             node = stack.pop();
#             node.val += preNum;
#             preNum = node.val;

#             if (node.left != null) {
#                 node = node.left;
#             } else {
#                 node = null;
#             }
#         } 
#         return root;
#     }
# }

