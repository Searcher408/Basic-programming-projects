# Python3
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 一次遍历
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        dummy = ListNode(0, head)
        cur = dummy # 从哑节点开始遍历

        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        
        return dummy.next

# 递归+迭代题解
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/solution/fu-xue-ming-zhu-di-gui-die-dai-yi-pian-t-wy0h/
# 递归
# 时间复杂度：O(N)，每个节点访问了一次。
# 空间复杂度：O(N)，递归调用的时候会用到了系统的栈。
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
        else:
            # move = head.next # 保留head便于后序使用head.val
            # while move and move.val == head.val: # 遍历至值不相等的节点为止，move可能为None
            #     move = move.next 
            # return self.deleteDuplicates(move) # move 之前的节点都不保留，值相等的节点都被删除

            x = head.val
            while head and head.val == x:
                head = head.next
            return self.deleteDuplicates(head)

        return head

# 迭代 一次遍历
# 时间复杂度：O(N)，对链表每个节点遍历了一次；
# 空间复杂度：O(1)，只使用了常量的空间。
class Solution: 
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0, head)
        pre = dummy
        cur = head
        
        while cur:
            # 跳过当前重复节点，使得cur指向当前重复元素的最后一个位置
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if pre.next == cur:
                # pre和cur之间没有重复节点，pre正常后移
                pre = pre.next
            else:
                # pre->next指向cur的下一个节点，相当于跳过当前的重复元素
                # 但是pre不移动，仍然指向已经遍历过的链表结尾
                pre.next = cur.next     
            cur = cur.next 
        return dummy.next

# 代码中用到了一个常用的技巧：dummy 节点，也叫做 哑节点。
# 它在链表的迭代写法中非常常见，因为可能会删除头结点，需要哑节点维护一个不变的头节点。

# 迭代，利用计数，两次遍历
# 这个做法忽略了链表有序这个性质，使用了两次遍历，
# 第一次遍历统计每个节点的值出现的次数，
# 第二次遍历的时候，如果发现 head.next 的 val 出现次数不是 1 次，则需要删除 head.next。
# 时间复杂度：O(N)，对链表遍历了两次；
# 空间复杂度：O(N)，需要一个字典保存每个节点值出现的次数。
class Solution: 
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        valList = []
        while head:
            valList.append(head.val)
            head = head.next
        counter = collections.Counter(valList) # 计算“可迭代序列中”各个元素的数量

        head = dummy
        while head and head.next:
            if counter[head.next.val] != 1:
                head.next = head.next.next
            else:
                head = head.next
        
        return dummy.next

