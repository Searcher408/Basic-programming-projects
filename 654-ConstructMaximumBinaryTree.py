# Python3
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        m = nums[0]
        n = 0
        for i in range(len(nums)):
            if nums[i] > m:
                m = nums[i]
                n = i
        
        node = TreeNode(m)
        node.left = self.constructMaximumBinaryTree(nums[:n])
        if n + 1 < len(nums):
            node.right = self.constructMaximumBinaryTree(nums[n+1:])
        # else:
        #     node.right = None

        return node

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        #递归
        if not nums:
            return None

        max_num = max(nums)
        max_idx = nums.index(max_num)

        root = TreeNode(max_num)
        root.left = self.constructMaximumBinaryTree(nums[:max_idx])
        root.right = self.constructMaximumBinaryTree(nums[max_idx+1:])

        return root 