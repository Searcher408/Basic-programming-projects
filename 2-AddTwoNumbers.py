# C++ 版本：
# class Solution {
# public:
# 	ListNode* addTwoNumbers(ListNode* l1, ListNode* l2){
# 		ListNode *head = nullptr, *tail = nullptr;
# 		int carry = 0;

# 		while(l1 || l2){
# 			int n1 = l1 ? l1->val : 0;
# 			int n2 = l2 ? l2->val : 0;
# 			int sum = n1 + n2 + carry;

# 			if(!head){
# 				head = tail = new ListNode(sum % 10);
# 			}else{
# 				tail->next = new ListNode(sum % 10);
# 				tail = tail->next;
# 			}

# 			carry = sum / 10;

# 			if(l1){
# 				l1 = l1->next;
# 			}
# 			if(l2){
# 				l2 = l2->next;
# 			}
# 		}

# 		if(carry > 0){
# 			tail->next = new ListNode(carry);
# 		}

# 		return head;
# 	}
# };

# //时间复杂度：O(max(m,n))，其中 m,n 为两个链表的长度。
# //我们要遍历两个链表的全部位置，而处理每个位置只需要 O(1)的时间。
# //空间复杂度：O(max(m,n))。
# //答案链表的长度最多为较长链表的长度 +1。

# Python 版本：
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 创建一个结点值为 None 的头结点, head 和 curr 指向头结点, head 用来最后返回, curr 用来遍历
        head = curr = ListNode(None)    # 变量head和curr是同一个链表节点的引用，对curr修改时，head的值也变了，因为它们指向同一个对象   
        carry = 0               		# 初始化进位 carry 为 0
        while l1 or l2 or carry:
            # 如果 l1 或 l2 存在, 则取l1的值 + l2的值 + carry(carry初始为0, 如果下面有进位1, 下次加上)
            carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)  
            curr.next = ListNode(carry % 10)    # curr.next 指向新链表节点
            curr = curr.next                    # curr 向后遍历
            carry //= 10                        # 有进位情况则取模, eg. carry = 18, 18 // 10 = 1
            l1 = l1.next if l1 else None    	# 如果l1存在, 则向后遍历, 否则为 None
            l2 = l2.next if l2 else None    	# 如果l2存在, 则向后遍历, 否则为 None
        return head.next   # 返回 head 的下一个节点, 因为 head 指向的是空的头结点, 下一个节点才是新建链表的后序节点

class Solution(object):
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		head = curr = ListNode(None)
		carry = val = 0 # carry 代表进位，val代表余值

		while carry or l1 or l2:
			val = carry

			if l1: l1, val = l1.next, l1.val + val
			if l2: l2, val = l2.next, l2.val + val

			carry, val = divmod(val, 10)
			curr.next = curr = ListNode(val) #等同于 curr.next  = ListNode(val) , curr = curr.next

		return head.next


# 在Python中可以使用连续赋值一次为多个变量进行赋值，比如：
# a = b = c = 1
# a, b, c = 1, 1, 1

# https://imliyan.com/blogs/article/Python%E8%BF%9E%E7%BB%AD%E8%B5%8B%E5%80%BC%E7%9A%84%E5%86%85%E9%83%A8%E5%8E%9F%E7%90%86/
# a = a.next = ListNode(1)
# 等同于
# _ = ListNode(1)  
# a = _
# a.next = _
# 注意：这里用_暂存了对象，整个过程中只创建了一个对象
# a = 3
# a, b = 1, a 	
# 此处b应该等于3
