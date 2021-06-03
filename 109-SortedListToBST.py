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

# 分治
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        