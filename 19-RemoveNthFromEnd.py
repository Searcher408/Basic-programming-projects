# Python3
# Definition for singly-linked list.
class ListNode:
    def __int__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first = head
        second = head 

        for _ in range(n):
            first = first.next

        if first == None: # 此时 n 为链表长度，倒数第 n 项即为第 1 项
            head = head.next
        else:
            while first.next != None:
                first = first.next
                second = second.next 
            # second 为倒数第 n+1 项， 需要删除倒数第 n 项
            second.next = second.next.next

        return head

# 在对链表进行操作时，一种常用的技巧是添加一个哑节点（dummy node），
# 它的 next 指针指向链表的头节点，这样就不需要对头节点进行特殊的判断。

class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def getLength(head: ListNode) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        dummy = ListNode(0, head)
        length = getLength(head)
        cur = dummy
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next

# C++ 计算链表长度
class Solution {
public:
    int getLength(ListNode* head) {
        int length = 0;
        while (head) {
            length++;
            head = head->next;
        }
        return length;
    }

    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(0, head);
        int length = getLength(head);

        ListNode* cur = dummy;
        for (int i = 1; i < length - n + 1; i++) {
            cur = cur->next;
        }

        cur->next = cur->next->next;
        ListNode* ans = dummy->next;

        delete dummy;
        return ans;
    }
};

# C++ 栈
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(0, head);
        stack<ListNode*> stk;

        ListNode* cur = dummy;
        while (cur) {
            stk.push(cur);
            cur = cur->next;
        }

        // 出栈至倒数第 n 项
        for (int i = 0; i < n; i++) {
            stk.pop();
        }

        ListNode* prev = stk.top(); //栈顶的节点就是待删除节点的前驱节点
        prev->next = prev->next->next;

        ListNode* ans = dummy->next;
        delete dummy;
        return ans;
    }
}

# Python3 栈 时间复杂度：O(L) 空间复杂度：O(L)，其中 L 是链表的长度，主要为栈的开销。
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        stack = list()
        cur = dummy
        while cur:
            stack.append(cur)
            cur = cur.next
        
        for i in range(n):
            stack.pop()

        prev = stack[-1]
        prev.next = prev.next.next

        return dummy.next

# Python3 双指针 时间复杂度：O(L) 空间复杂度：O(1)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next

