# Python3
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        nums = []
        for list in lists:
            while list:
                nums.append(list.val)
                list = list.next
        
        nums.sort()
        dummy = ListNode(0)
        cur = dummy
        while nums:
            node = ListNode(nums.pop(0))
            cur.next = node
            cur = node
        
        return dummy.next

# 分治
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        n = len(lists)
        m = n // 2
        if n == 1:
            return lists[0]
        
        a = self.mergeKLists(lists[:m])
        b = self.mergeKLists(lists[m:])
        dummy = ListNode(0)
        cur = dummy
        while a and b:
            if a.val < b.val:
                cur.next = a
                a = a.next 
            else:
                cur.next = b
                b = b.next
            cur = cur.next
        cur.next = a if a else b

        return dummy.next


# 用容量为K的最小堆优先队列，把链表的头结点都放进去，然后出队当前优先队列中最小的，挂上链表，
# 然后让出队的那个节点的下一个入队，再出队当前优先队列中最小的，直到优先队列为空。
# Java
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) {
            return null;
        }

        ListNode dummyHead = new ListNode(0);
        ListNode curr = dummyHead;
        PriorityQueue<ListNode> pq = new PriorityQueue<>(new Comparator<ListNode>() {
            @Override
            public int compare(ListNode l1, ListNode l2) {
                return l1.val - l2.val; // l1.val - l2.val < 0 , 则l1优先级高
            }
        });

        for (ListNode list : lists) {
            if (list == numll) {
                continue;
            }
            pq.add(list);
        }

        while (!pq.isEmpty()) {
            ListNode nextNode = pq.poll();
            curr.next = nextNode;
            curr = curr.next;
            if (nextNode.next != null) {
                pq.add(nextNode.next);
            }
        }

        return dummyHead.next;
    }
}

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        dummy = ListNode(0)
        p = dummy
        heap = [] # 最小堆优先队列
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        
        while heap:
            val, idx = heapq.heappop(heap)
            p.next = ListNode(val) # 增大了内存消耗
            p = p.next
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        
        return dummy.next

# Python的富比较方法包括__lt__、__gt__分别表示：小于、大于
# 当自定义类中两个方法都定义了时，“<”、“>”分别调用__lt__和__gt__方法
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def __lt__(self, other):
            return self.val < other.val
        ListNode.__lt__ = __lt__
    
        import heapq
        heap = []
        dummy = ListNode(-1)
        p = dummy

        for l in lists:
            if l:
                heapq.heappush(heap, l)
        
        while heap:
            p.next = heapq.heappop(heap)
            p = p.next
            if p.next:
                heapq.heappush(heap, p.next)
        
        return dummy.next

# 合并两个有序链表 时间复杂度：O(n), 空间复杂度：O(1)。
# C++
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
}

ListNode* mergeTwoLists(ListNode *a, ListNode *b) {
    if ((!a) || (!b)) {
        return a ? a : b;
    }
    ListNode head, *tail = &head, *aPtr = a, *bPtr = b;
    while (aPtr && bPtr) {
        if (aPtr->val < bPtr->val) {
            tail->next = aPtr;
            aPtr = aPtr->next;
        } else {
            tail->next = bPtr;
            bPtr = bPtr->next;
        }
        tail = tail->next;
    }
    tail->next = (aPtr ? aPtr : bPtr);
    return head.next;
}

# 顺序合并
class Solution {
public:
    ListNode* mergeTwoLists(ListNode *a, ListNode *b) {
        if ((!a) || (!b)) {
            return a ? a : b;
        }
        ListNode head, *tail = &head, *aPtr = a, *bPtr = b;
        while (aPtr && bPtr) {
            if (aPtr->val < bPtr->val) {
                tail->next = aPtr;
                aPtr = aPtr->next;
            } else {
                tail->next = bPtr;
                bPtr = bPtr->next;
            }
            tail = tail->next;
        }
        tail->next = (aPtr ? aPtr : bPtr);
        return head.next;
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode *ans = nullptr;
        for (size_t i = 0; i < lists.size(); i++) {
            ans = mergeTwoLists(ans, lists[i]);
        }
        return ans;
    }
};

# 分治合并
# 将 k 个链表配对并将同一对中的链表合并
class Solution {
public:
    ListNode* mergeTwoLists(ListNode *a, ListNode *b) {
        if ((!a) || (!b)) {
            return a ? a : b;
        }
        ListNode head, *tail = &head, *aPtr = a, *bPtr = b;
        while (aPtr && bPtr) {
            if (aPtr->val < bPtr->val) {
                tail->next = aPtr;
                aPtr = aPtr->next;
            } else {
                tail->next = bPtr;
                bPtr = bPtr->next;
            }
            tail = tail->next;
        }
        tail->next = (aPtr ? aPtr : bPtr);
        return head.next;
    }

    ListNode* merge(vector<ListNode*> &lists, int l, int r) {
        if (l == r) {
            return list[l];
        }
        if (l > r) {
            return nullptr;
        }
        int mid = (l + r) >> 1;
        return mergeTwoLists(merge(lists, l, mid), merge(lists, mid + 1, r));
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        return merge(lists, 0, lists.size() - 1);
    }
};

# 使用优先级队列合并
class Solution {
public:
    struct Status {
        int val;
        ListNode *ptr;
        bool operator < (const Status &rhs) const {
            return val > rhs.val;
        }
    };

    priority_queue<Status> q;

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        for (auto node : lists) {
            if (node) {
                q.push({node->val, node});
            }
        }
        ListNode head, *tail = &head;
        while (!q.empty()) {
            auto f = q.top();
            q.pop();
            tail->next = f.ptr;
            tail = tail->next;
            if (f.ptr->next) {
                q.push({f.ptr->next->val, f.ptr->next});
            }
        }
        return head.next;
    }
};