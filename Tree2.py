# Python3
from collections import deque

class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

# 把有序数组转换为二叉树
def arrayToTree(arr, start, end):
    root = None
    if end >= start:
        root = BiTNode()
        mid = (start + end + 1) // 2
        root.data = arr[mid]
        root.lchild = arrayToTree(arr, start, mid - 1)
        root.rchild = arrayToTree(arr, mid + 1, end)
    else:
        root = None
    
    return root

# 用层序遍历打印二叉树节点
def printTreeLayer(root):
    if root == None:
        return
    
    queue = deque()
    queue.append(root) # 树根节点进队列

    while len(queue) > 0:
        p = queue.popleft()
        print(p.data) # 访问当前节点

        if p.lchild != None: # 左孩子不为空则入队列
            queue.append(p.lchild)
        
        if p.rchild != None: # 右孩子不为空则入队列
            queue.append(p.rchild)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    root = arrayToTree(arr, 0, len(arr) - 1)

    printTreeLayer(root)