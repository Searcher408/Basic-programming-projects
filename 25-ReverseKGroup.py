# Python3
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 递归
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 1:
            return head

        ret = head 
        for _ in range(k-1): # ret遍历至第k个节点，用于后续返回头节点
            if not ret.next:
                return head
            else:
                ret = ret.next

        cur = head.next
        pre = head
        for _ in range(k-1): # 修改k-1个节点的next指针，最终pre为第k个节点，cur为第k+1个节点
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        
        head.next = self.reverseKGroup(cur, k)
        head = ret # 返回头节点

        return head       

# 迭代
# 时间复杂度：O(n)，其中 n 为链表的长度。空间复杂度：O(1)，只需要建立常数个变量。
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0, head)
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            
            nextTmp = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新拼接
            pre.next = head 
            tail.next = nextTmp
            pre = tail # 新的一轮分组
            head = tail.next
    
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode):
        pre = tail.next # 初始值设置为tail.next，用于赋值给head.next
        cur = head
        while pre != tail:
            nextTmp = cur.next
            cur.next = pre
            pre = cur
            cur = nextTmp
        return tail, head

        