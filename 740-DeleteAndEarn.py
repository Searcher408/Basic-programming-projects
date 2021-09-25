# Python3
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        maxVal = max(nums)
        total = [0] * (maxVal + 1)
        for val in nums:
            total[val] += val
        
        def rob(nums: List[int]) -> int:
            size = len(nums)
            first, second = nums[0], max(nums[0], nums[1])
            for i in range(2, size):
                first, second = second, max(first + nums[i], second)
            return second
        
        return rob(total)

# C++
# 记元素 x 在数组中出现的次数为 c_x, 用一个数组 sum 记录数组 nums 中所有相同元素之和，
# 即 sum[x]=x⋅c_x, 若选择了 x，则可以获取 sum[x] 的点数，且无法再选择 x-1 和 x+1。
# 这与「198. 打家劫舍」是一样的。
class Solution {
private:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) {
            return nums[0];
        }
        int first = nums[0], second = max(nums[0], nums[1]);
        for (int i = 2; i < n; i++) {
            int tmp = second;
            second = max(first + nums[i], second);
            first = tmp;
        }
        return second;
    }

public:
    int deleteAndEarn(vector<int>& nums) {
        int maxVal = 0;
        for (int val : nums) {
            maxVal = max(maxVal, val);
        }
        vector<int> sum(maxVal + 1);
        for (int val : nums) {
            sum[val] += val;
        }
        return rob(sum);
    }
};