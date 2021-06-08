# Python3
class Stack(object):
    # 初始化栈为空列表
    def __init__(self):
        self.items = []

    # 判断栈是否为空，返回布尔值
    def is_empty(self):
        return self.items == []

    # 返回栈顶元素
    def peek(self):
        return self.items[len(self.items) - 1]

    # 返回栈的大小
    def size(self):
        return len(self.items)

    # 把新的元素堆进栈里面
    def push(self, item):
        self.items.append(item)

    # 删除栈顶元素
    def pop(self, item):
        return self.items.pop()

def main():
    myStack = Stack()
    myStack.push('h')
    print(myStack.size())

if __name__ == "__main__":
    main()