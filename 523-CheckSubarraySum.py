# Python3
from typing import List

# 超时
class Solution: 
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums) 
        if n < 2: # 题目要求子数组大小至少为 2
            return False

        dp = [[num for num in nums] for i in range(n-1)]

        for i in range(n-1):
            for j in range(i+1, n):
                dp[i][j] += dp[i][j-1]
                if dp[i][j] % k == 0:
                    return True
        return False 

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n < 2:
            return False
        
        mp = dict()
        mp[0] = -1
        remainder = 0
        for i in range(n):
            remainder = (remainder + nums[i]) % k
            if remainder in mp:
                preIndex = mp[remainder]
                if i - preIndex >= 2:
                    return True
            else:
                mp[remainder] = i
        return False


if __name__ == "__main__":
    test = Solution()
    # nums = [23,2,6,4,7]
    # k = 13
    nums = [0]
    k = 1
    res = test.checkSubarraySum(nums, k)
    print(res)

# 前缀和 + 哈希表
# 事先计算出数组 nums 的前缀和数组，则对于任意一个子数组，都可以在 O(1) 的时间内得到其元素和。
# 当 prefixSums[q]−prefixSums[p] 为 k 的倍数时，prefixSums[p] 和 prefixSums[q] 除以 k 的余数相同。

# 由于哈希表存储的是每个余数第一次出现的下标，因此当遇到重复的余数时，根据当前下标和哈希表中存储的下标
# 计算得到的子数组长度是以当前下标结尾的子数组中满足元素和为 k 的倍数的子数组长度中的最大值。
# 只要最大长度至少为 22，即存在符合要求的子数组。
# Java
class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        int m = nums.length;
        if (m < 2) {
            return false;
        }
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        map.put(0, -1);
        int remainder = 0;
        for (int i = 0; i < m; i++) {
            remainder = (remainder + nums[i]) % k;
            if (map.containsKey(remainder)) {
                int prevIndex = map.get(remainder);
                if (i - preIndex >= 2) {
                    return true;
                }
            } else {
                map.put(remainder, i);
            }
        }
        return false;
    }
}

# C++
class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        int m = nums.size();
        if (m < 2) {
            return false;
        }
        unordered_map<int, int> mp;
        mp[0] = -1;
        int remainder = 0;
        for (int i = 0; i < m; i++) {
            remainder = (remainder + nums[i]) % k;
            if (mp.count(remainder)) {
                int preIndex = mp[remainder];
                if (i - preIndex >= 2) {
                    return true;
                }
            } else {
                mp[remainder] = i;
            }
        }
        return false;
    }
};