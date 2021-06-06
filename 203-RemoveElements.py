# Python3
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 迭代
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None

        dummy = ListNode(0, head)
        pre = dummy
        while head:
            if head.val == val:
                tmp = head.next
                pre.next = head.next
                head = tmp
                continue
            head = head.next
            pre = pre.next
        
        return dummy.next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None

        dummy = ListNode(0, head)
        pre = dummy
        while pre.next:
            if pre.next.val == val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        
        return dummy.next

# 递归
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        
        if head.val == val:
            head = self.removeElements(head.next, val)
        else:
            head.next = self.removeElements(head.next, val)
        
        return head

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head