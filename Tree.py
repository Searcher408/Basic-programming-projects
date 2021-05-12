# Python3
class BinTreeNode(object):
    def __init__(self, data, left = None, right = None):
        self.data, self.left, self.right = data, left, right

class BinTree(object):
    def __init__(self, root = None):
        self.root = root

    @classmethod
    def buildFrom(cls, nodeList):
        '''
        通过节点信息构造二叉树
        第一次遍历构造 node 节点
        第二次遍历给 root 和 孩子赋值
        param nodeList: {'data': 'A', 'left': None, 'right': None, 'is_root': False}
        '''
        nodeDict= {}
        for nodeData in nodeList:
            data = nodeData['data']
            nodeDict[data] = BinTreeNode(data)

        for nodeData in nodeList:
            data = nodeData['data']
            node = nodeDict[data]
            if nodeData['is_root']:
                root = node
            node.left = nodeDict.get(nodeData['left'])
            node.right = nodeDict.get(nodeData['right'])
        
        return cls(root)
    
    def preOrder(self, subtree):
        if subtree is not None:
            print(subtree.data)
            self.preOrder(subtree.left)
            self.preOrder(subtree.right)


nodeList = [
    {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
    {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
    {'data': 'D', 'left': None, 'right': None, 'is_root': False},
    {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
    {'data': 'H', 'left': None, 'right': None, 'is_root': False},
    {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
    {'data': 'F', 'left': None, 'right': None, 'is_root': False},
    {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
    {'data': 'I', 'left': None, 'right': None, 'is_root': False},
    {'data': 'J', 'left': None, 'right': None, 'is_root': False},
]

btree = BinTree.buildFrom(nodeList)
btree.preOrder(btree.root)
