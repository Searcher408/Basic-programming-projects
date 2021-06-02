# Python3
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 时间复杂度: O(n)，其中 n 是原链表的长度，对该链表进行了一次遍历。空间复杂度: O(1)。
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        node1 = dummy1 # 链接小于x的节点
        node2 = dummy2 # 链接大于等于x的节点

        while head:
            if head.val < x:
                node1.next = head
                node1 = node1.next
            else:
                node2.next = head
                node2 = node2.next
            head = head.next
        
        node2.next = None
        node1.next = dummy2.next

        return dummy1.next


            
            
                 
