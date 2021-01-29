# C++ 版本
# class Solution {
# public:
#     int lengthOfLongestSubstring(string s) {
#         // 哈希集合，记录每个字符是否出现过
#         unordered_set<char> loopup;
#         int n = s.size();

#         // 右指针，初始值为 -1，相当于在字符串的左边界，还没有开始移动
#         int rk = -1, ans = 0;//ans记录子串的最大长度

#         // 枚举左指针的位置，初始值隐性地表示为 -1
#         for (int i = 0; i < n; i++) {
#             if (i != 0) {
#                 // 左指针向右移动一格，移除一个字符
#                 loopup.erase(s[i - 1]);
#             }
#             while (rk + 1 < n && !loopup.count(s[rk + 1])) {
#                 // 不断地移动右指针
#                 loopup.insert(s[rk + 1]);
#                 rk++;
#             }
#             // 第 i 到 rk 个字符是最大长度的无重复字符子串
#             ans = max(ans, rk - i + 1);
#         }
#         return ans;
#     }
# };

# 「滑动窗口」使用两个指针表示字符串中的某个子串（的左右边界），其中左指针代表「枚举子串的起始位置」，
# 右指针为r_k；每一步操作中，将左指针向右移动一格，表示开始枚举下一个字符作为起始位置，然后不断地向右移动右指针，
# 需要保证这两个指针对应的子串中没有重复的字符。移动结束后这个子串就对应着以左指针开始的，不包含重复字符的最长子串。

# 本题需要使用一种数据结构来判断是否有重复的字符，常用的数据结构为哈希集合（即 C++ 中的 std::unordered_set，
# Java 中的 HashSet，Python 中的 set, JavaScript 中的 Set）。在左指针向右移动的时候，则从哈希集合中移除一个字符；
# 在右指针向右移动的时候，则往哈希集合中添加一个字符。

# 时间复杂度：O(N)，其中 N 是字符串的长度。左指针和右指针分别会遍历整个字符串一次。

# 空间复杂度：O(|Σ|)，其中Σ表示字符集(即字符串中可以出现的字符),|Σ|表示字符集的大小。
# 本题字符集默认为所有 ASCII 码在[0,128) 内的字符，即|Σ|=128。
# 由于需要用到哈希集合来存储出现过的字符，而字符最多有|Σ|个，因此空间复杂度为 O(|Σ|)。

# Python 版本
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # 哈希集合，记录每个字符是否出现过
#         loopup = set() #set() 函数创建一个无序不重复元素集
#         n = len(s)

#         # 右指针，初始值为 -1，相当于在字符串的左边界，还没有开始移动
#         rk, ans = -1, 0
#         for i in range(n):
#             if i != 0:
#                 # 左指针向右移动一格，移除一个字符
#                 loopup.remove(s[i - 1])
#             while rk + 1 < n and s[rk + 1] not in loopup:
#                 # 不断地移动右指针
#                 loopup.add(s[rk + 1])
#                 rk += 1
#             # 第 i 到 rk 个字符是一个极长的无重复字符子串
#             ans = max(ans, rk - i + 1)
#         return ans

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if not s: return 0 #空字符串返回长度0
#         left = 0
#         lookup = set()
       
#         max_len = 0
#         cur_len = 0
#         for i in s:
#             cur_len += 1
#             while i in lookup: # 当重复字符一直在集合中则一直循环，直到集合删除该字符
#                 lookup.remove(s[left])
#                 #print("remove:"+s[left])
#                 left += 1 #左指针右移
#                 cur_len -= 1
#             if cur_len > max_len: max_len = cur_len
#             lookup.add(i)
#         return max_len

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        max_len = 0            # 最大长度
        lookup = []            # 放字符串的一个队列    
        for i in s:
            while i in lookup:
                del lookup[0]  # 删除队列左边第一个，直到没有重复的字符串
            lookup.append(i)       
            if len(lookup) > max_len: max_len = len(lookup)
        return max_len

def main():
	test = Solution()
	ans = test.lengthOfLongestSubstring("pwwkew")
	print(ans)

if __name__ == "__main__":
	main()
