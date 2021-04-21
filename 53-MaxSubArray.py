# Python3
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        maxNum = - 100001

        for i in range(n):
            dp[i][i] = nums[i]
        
        for i in range(n):
            for j in range(i+1, n):
                dp[i][j] = dp[i][j-1] + nums[j]
        
        for i in range(n):
            for j in range(i, n):
                if dp[i][j] > maxNum:
                    maxNum = dp[i][j]

        return maxNum

# 动态规划转移方程: f(i) = max {f(i-1) + nums[i], nums[i]}
# 时间复杂度O(n), 空间复杂度O(1)
# C++
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int pre = 0, maxAns = nums[0];
        for (const auto &x: nums) {
            pre = max(pre + x, x);
            maxAns = max(maxAns, pre);
        }
        return maxAns;
    }    
};

# Python3
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        sum = 0
        maxAns = nums[0]
        for i in range(n):
            # sum = max(sum + nums[i], nums[i])
            sum += nums[i]
            if sum < nums[i]:
                sum = nums[i]
            
            # maxAns = max(maxAns, sum)
            if sum > maxAns:
                maxAns = sum

        return maxAns

# Java
class Solution {
    public int maxSubArray(int[] nums) {
        int pre = 0, maxAns = nums[0];
        for (int x : nums) {
            pre = Math.max(pre + x, x);
            maxAns = Math.max(maxAns, pre);
        }
        return maxAns;
    }
}

# 分治
# 对于一个区间 [l, r], 维护四个量：
# lSum 表示 [l, r] 内以 l 为左端点的最大子段和
# rSum 表示 [l, r] 内以 r 为右端点的最大子段和
# mSum 表示 [l, r] 内的最大子段和
# iSum 表示 [l, r] 的区间和
# C++ 线段树
class Solution {
public:
    struct Status {
        int lSum, rSum, mSum, iSum;
    };

    Status pushUp(Status l, Status r) {
        int iSum = l.iSum + r.iSum; 
        int lSum = max(l.lSum, l.iSum + r.lSum);
        int rSum = max(r.rSum, r.iSum + l.rSum);
        int mSum = max(max(l.mSum, r.mSum), l.rSum + r.lSum);

        return (Status) {lSum, rSum, mSum, iSum};
    }

    Status get(vector<int> &a, int l, int r) {
        if (l == r) {
            return (Status) {a[l], a[l], a[l], a[l]};
        }
        int m = (l + r) >> 1;
        Status lSub = get(a, l, m);
        Status rSub = get(a, m+1, r);
        return pushUp(lSub, rSub);
    }

    int maxSubArray(vector<int>& nums) {
        return get(nums, 0, nums.size()-1).mSum;
    }
};

