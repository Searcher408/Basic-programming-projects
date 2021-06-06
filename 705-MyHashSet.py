# 设计应该包含以下的功能:
# add(value)：向哈希集合中插入一个值。
# contains(value) ：返回哈希集合中是否存在这个值。
# remove(value)：将给定值从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。

# class HashSet:
#     def __init__(self):
#         self.set = set([])
    
#     def add(self, key: int) -> None:
#         self.set.add(key)
    
#     def remove(self, key: int) -> None:
#         if self.contains(key):
#             self.set.remove(key)
        
#     def contains(self, key: int) -> bool:
#         return key in self.set

# 创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

# class HashSet:
#     def __init__(self):
#         self.set = []

#     def add(self, key: int) -> None:
#         if not self.contains(key):
#             self.set.append(key)

#     def remove(self, key: int) -> None:
#         if self.contains(key):
#             self.set.remove(key)

#     def contains(self, key: int) -> bool:
#         """
#         Returns true if this set contains the specified element
#         """
#         return key in self.set

# 实现哈希集合的关键问题：
# 哈希函数
# 冲突处理（链地址法，开放地址法，再哈希法）
# 扩容
class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mod = 769
        self.bucket = [[] for _ in range(self.mod)]

    def add(self, key: int) -> None:
        k = key % self.mod
        if key not in self.bucket[k]:
            self.bucket[k].append(key)

    def remove(self, key: int) -> None:
        k = key % self.mod
        if key in self.bucket[k]:
            self.bucket[k].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        k = key % self.mod
        return key in self.bucket[k]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# C++ 
# 设哈希表的大小为 base，哈希函数：hash(x) = x mod base。
# 使用整数除法作为哈希函数，为了尽可能避免冲突，将 base 取为一个质数
# 链地址法处理冲突
class MyHashSet {
private:
    vector<list<int>> data;
    static const int base = 769;
    static int hash(int key) {
        return key % base;
    }
public:
    /** Initialize your data structure here. */
    MyHashSet(): data(base) {

    }
    
    void add(int key) {
        int h = hash(key);
        for (auto it = data[h].begin(); it != data[h].end(); it++) {
            if ((*it) == key) {
                return;
            }
        }
        data[h].push_back(key);
    }
    
    void remove(int key) {
        int h = hash(key);
        for (auto it = data[h].begin(); it != data[h].end(); it++) {
            if ((*it) == key) {
                data[h].erase(it);
                return;
            }
        }
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        int h = hash(key);
        for (auto it = data[h].begin(); it != data[h].end(); it++) {
            if ((*it) == key) {
                return true;
            }
        }
        return false;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */