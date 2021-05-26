#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Python 3
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# 递归 https://lyl0724.github.io/2020/01/25/1/
# 时间复杂度：O(n)，其中 n 是链表的节点数量。需要对每个节点进行更新指针的操作。
# 空间复杂度：O(n)，其中 n 是链表的节点数量。空间复杂度主要取决于递归调用的栈空间。
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        # subHead 是 head.next.next 之后的节点两两交换后的头节点
        subHead = self.swapPairs(head.next.next) 
        headNext = head.next
        headNext.next = head
        head.next = subHead

        return headNext
    
# 迭代法
# 时间复杂度：O(n)，其中 n 是链表的节点数量。需要对每个节点进行更新指针的操作。
# 空间复杂度：O(1)。
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyHead = ListNode()
        dummyHead.next = head # 引入虚拟头节点dummyHead，其下一个节点初始为节点head
        prev = dummyHead # 定义变量prev，初始指向虚拟头节点dummyHead

        # 只有当prev指向的节点之后有两个节点时才需要交换
        while prev.next != None and prev.next.next != None:
            node1 = prev.next
            node2 = prev.next.next
            subHead = node2.next

            node2.next = node1
            node1.next = subHead
            prev.next = node2 # 很重要，能够将每两个交换后的节点连接起来

            # prev指向交换后节点的第二个，即未交换的前一个节点
            prev = node1
        
        return dummyHead.next

# 递归是一个反复调用自身的过程，这就说明它每一级的功能都是一样的，因此只需要关注一级递归的解决过程即可。
# 解递归题的三部曲：
# 1.找整个递归的终止条件：递归应该在什么时候结束？
# 2.找返回值：应该给上一级返回什么信息？
# 3.本级递归应该做什么：在这一级递归中，应该完成什么任务？

# 1.找终止条件。 
# 什么情况下递归终止？无法交换的时候，递归就终止了。因此当链表只剩一个节点或者没有节点的时候，自然递归就终止了。
# 2.找返回值。 
# 目的是两两交换链表中相邻的节点，因此自然希望返回给上一级递归的是已经完成交换处理，即已经处理好的链表。
# 3.本级递归应该做什么。 
# 结合第二步，由于只考虑本级递归，所以这个链表在我们眼里其实也就三个节点：head、head.next、已处理完的链表部分。
# 而本级递归的任务也就是交换这3个节点中的前两个节点
# Java
class Solution {
    public ListNode swapPairs(ListNode head) {
        if(head == null || head.next == null) {
            return head;
        }

        ListNode next = head.next;
        head.next = swapPairs(next.next);
        next.next = head;

        return next; // 返回给上一级的是当前已经完成交换后，即处理好了的链表部分
    }
}