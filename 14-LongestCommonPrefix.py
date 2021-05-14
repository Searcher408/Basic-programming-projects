# Python3
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        利用python的max()和min()对字符串进行比较，结果按照ascII值排序
        举例abb，aba，abac，最大为abb，最小为aba。
        所以只需要比较最大最小的公共前缀就是整个数组的公共前缀
        '''
        if not strs:
            return ""
        
        s1 = min(strs)
        s2 = max(strs)

        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        
        return s1

    def longestCommonPrefix1(self, strs):
        if not strs:
            return ""
        
        s = list(map(set, zip(*strs))) # [{'f'}, {'l'}, {'o', 'i'}, {'g', 'w'}]
        res = ""

        for i, x in enumerate(s):
            x = list(x)
            # print(x)
            if len(x) > 1:
                break
            res = res + x[0]
        
        return res

def main():
    test = Solution()
    strs = ["flower","flow","flight"]
    res = test.longestCommonPrefix1(strs)
    print(res)
    
    # a = [1, 3, 5, 7]
    # b = [2, 4, 6]
    # zipped = zip(a, b)
    # nums = list(zipped)
    # print(nums) # [(1, 2), (3, 4), (5, 6)]

    # c, d = zip(*zip(a, b))
    # print(list(c)) # [1, 3, 5]
    # print(list(d)) # [2, 4, 6]

    # 使用 lambda 匿名函数计算列表各个元素的平方, 并使用 list() 转换为列表
    # nums = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))   
    # print(nums) # [1, 4, 9, 16, 25]

    # strs = ["flower","flow","flight"]
    # print(list(zip(*strs))) # [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
    # strList = list(map(set, zip(*strs)))
    # print(strList) # [{'f'}, {'l'}, {'o', 'i'}, {'g', 'w'}]

if __name__ == "__main__":
    main()

# typing模块的作用：
# 类型检查，防止运行时出现参数和返回值类型不对的情况
# 作为开发文档附加说明，方便使用函数时传入和返回正确的参数，利于开发效率
# 该模块并不会实际影响到程序的运行，不会报错，但是会有提示。

# typing常用类型：
# int, long, float: 整型,长整型,浮点型;
# bool, str: 布尔型，字符串类型;
# List, Tuple, Dict, Set:列表，元组，字典, 集合;
# Iterable,Iterator:可迭代类型，迭代器类型;
# Generator：生成器类型。

# 横向扫描 时间复杂度：O(mn)，m是字符串数组中的字符串的平均长度，n是字符串的数量。空间复杂度：O(1)
# 依次遍历字符串数组中的每个字符串，
# 对于每个遍历到的字符串，更新最长公共前缀，
# 当遍历完所有的字符串以后，即可得到字符串数组中的最长公共前缀。
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break

        return prefix

    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]

# 纵向扫描 时间复杂度：O(mn)，m是字符串数组中的字符串的平均长度，n是字符串的数量。空间复杂度：O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            if any(i == len(strs[j])) or strs[j][i] != c for j in range(1, count):
                return strs[0][:i]
        
        return strs[0]
    
# Python any() 函数，如果都为空、0、false，则返回false；如果不都为空、0、false，则返回true。

# 分治 时间复杂度：O(mn) 空间复杂度：O(mlogn)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def lcp(start, end):
            if start == end:
                return strs[start]

            mid = (start + end) // 2
            lcpLeft, lcpRight = lcp(start, mid), lcp(mid + 1, end)
            mimLength = min(len(lcpLeft), len(lcpRight))

            for i in range(mimLength):
                if lcpLeft[i] != lcpRight[i]:
                    return lcpLeft[:i]

            return lcpLeft[:mimLength]

        return "" if not strs else lcp(0, len(strs) - 1)

# 二分查找 
# 时间复杂度：O(mnlogm) 二分查找的迭代执行次数是 O(logm)，每次迭代最多需要比较 mn 个字符
# 空间复杂度：O(1)。使用的额外空间复杂度为常数。
# 最长公共前缀的长度不会超过字符串数组中的最短字符串的长度。
# 用 minLength 表示字符串数组中的最短字符串的长度，
# 则可以在[0,minLength] 的范围内通过二分查找得到最长公共前缀的长度。
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def isCommonPrefix(length):
            str0, count = str[0][:length], len(strs)
            return all(strs[i][:length] == str0 for i in range(1, count))

        if not strs:
            return ""
        
        minLength = min(len(s) for s in strs)
        low, high = 0, minLength

        while low < high:
            mid = (high - low + 1) // 2 + low
            if isCommonPrefix(mid):
                low = mid
            else:
                high = mid - 1

        return strs[0][:low]

# all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
# 元素除了是 0、空、None、False 外都算 True。

