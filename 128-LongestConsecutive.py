# Python3
from typing import List

# 哈希表
# 外层循环需要 O(n) 的时间复杂度，只有当一个数是连续序列的第一个数的情况下才会进入内层循环，
# 然后在内层循环中匹配连续序列中的数，因此数组中的每个数只会进入内层循环一次。总时间复杂度为 O(n)
# 空间复杂度：O(n)。哈希表存储数组中所有的数需要 O(n) 的空间。
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        numSet = set(nums)

        for num in numSet:
            if num - 1 not in numSet:
                curNum = num
                curLen = 1

                while curNum + 1 in numSet:
                    curNum += 1
                    curLen += 1
                
                maxLen = max(maxLen, curLen)
        
        return maxLen

# 动态规划
# 题目要求 O(n) 复杂度。用哈希表存储每个端点值对应连续区间的长度。
# 若数已在哈希表中：跳过不做处理
# 若是新数加入：
#   取出其左右相邻数已有的连续区间长度 left 和 right
#   计算当前数的区间长度为：curLen = left + right + 1
#   根据 curLen 更新最大长度 maxLen 的值
#   更新区间两端点的长度值
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashDict = dict()

        maxLen = 0
        for num in nums:
            if num not in hashDict:
                left = hashDict.get(num - 1, 0)
                right = hashDict.get(num + 1, 0)

                curLen = left + right + 1
                if curLen > maxLen:
                    maxLen = curLen
                
                hashDict[num] = curLen # 标记num已经在hash中，可以是随便一个值
                hashDict[num - left] = curLen # 重要的是更新端点的值
                hashDict[num + right] = curLen
        
        return maxLen

# dict.get(key, default=None)
# key -- 字典中要查找的键。
# default -- 如果指定键的值不存在时，返回该默认值。

# 并查集是一种树形的数据结构，它支持两种操作：
# 查找（Find）：确定某个元素处于哪个子集；
# 合并（Union）：将两个子集合并成一个集合。
# 并查集不支持集合的分离，但是并查集在经过修改后可以支持集合中单个元素的删除操作。

# C++ 采用并查集的路径压缩这一策略
# 初始化的时候先把数组里每个元素初始化为它的下一个数，合并时查找它能到达的最远的数字就可以了。
class Solution {
public:
    unordered_map<int, int> fa;

    int find(int x) {
        return fa.count(x) ? (fa[x] = find(fa[x])) : x;
    }

    int longestConsecutive(vector<int>& nums) {
        for (auto i : nums) {
            fa[i] = i + 1;
        }

        int ans = 0;
        for (auto i : nums) {
            int y = find(i + 1);
            ans = max(ans, y - i);
        }

        return ans;
    }
};

# C++ 迭代
# 连续的子序列只需要遍历最小的元素就可以了
# 倒着遍历是因为每次计算 size() 也会耗费一点时间
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int, int> fa;
        for (auto i : nums) {
            fa[i] = i; # 标记i已经在map中，可以是随便一个值
        }
        int ans = 0;
        for (int i = nums.size() - 1; i >= 0; i--) {
            if (!fa.count(nums[i] - 1)) {
                int cur = nums[i];
                while (fa.count(cur + 1)) {
                    cur++;
                }
                ans = max(ans, cur - nums[i] + 1);
            }
        }
        return ans;
    }
};