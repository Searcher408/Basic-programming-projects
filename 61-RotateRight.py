# Python3
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
            
        p1 = head
        p2 = head
        
        for _ in range(k):
            if not p1.next: # k超过链表的长度
                p1 = head
            else:
                p1 = p1.next
        
        while p1.next:
            p1 = p1.next
            p2 = p2.next
         
        p1.next = head
        head = p2.next
        p2.next = None # 末尾节点的next置空
        
        return head

# 执行结果：超出时间限制
# 最后执行的输入：
# [1,2,3]
# 2000000000    

# 旋转链表，本质上是将尾部向前数第K个元素作为头，原来的头接到原来的尾上
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
            
        p1 = head
        p2 = head
        tmp = head
        
        n = 0
        while tmp: # 计算链表长度
            tmp = tmp.next
            n += 1
        
        for _ in range(k%n):
            p1 = p1.next
        
        while p1.next:
            p1 = p1.next
            p2 = p2.next
         
        p1.next = head
        head = p2.next
        p2.next = None # 末尾节点的next置空
        
        return head

# 先将给定的链表连接成环，然后将指定位置断开
# 首先计算出链表的长度 nn，并找到该链表的末尾节点，将其与头节点相连。
# 然后找到新链表的最后一个节点（即原链表的第(n−1)−(k mod n)个节点），将当前闭合为环的链表断开
# 特别地，当链表长度不大于 1，或者 k 为 n 的倍数时，新链表将与原链表相同
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head or not head.next:
            return head
        
        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1
        
        if k%n == 0:
            return head
           
        cur.next = head # 成环
        add = n - k%n
        while add:
            cur = cur.next # 从head开始遍历至新链表的最后一个节点
            add -= 1
        ret = cur.next
        cur.next = None

        return ret
