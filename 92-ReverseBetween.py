# Python3
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = 0
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        if not head or not head.next or left == right:
            return head
        
        dummy = ListNode(0, head)
        hair = tail = dummy
        for i in range(right):
            if i < left - 1:
                hair = hair.next
            tail = tail.next
        # head = [1,2,3,4,5], left = 2, right = 4
        # hair = 1, tail = 4

        tmp = hair.next
        hair.next = tail
        hair = tmp
        pre = tail.next
        
        for _ in range(left, right+1):
            tmp = hair.next
            hair.next = pre
            pre = hair
            hair = tmp
        
        return dummy.next

# 只遍历一次，头插法
# 整体思想是：在需要反转的区间里，每遍历到一个节点，让这个新节点来到反转部分的起始位置。
# curr：指向待反转区域的第一个节点 left；
# next：永远指向 curr 的下一个节点，循环过程中，curr 变化以后 next 会变化；
# pre：永远指向待反转区域的第一个节点 left 的前一个节点，在循环过程中不变。
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(-1, head)
        pre = dummy

        for _ in range(left - 1):
            pre = pre.next
        
        cur = pre.next
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        
        return dummy.next

    

        
