# Python3
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def robRange(start: int, end: int) -> int:
            first = nums[start]
            second = max(nums[start], nums[start + 1])
            for i in range(start + 2, end + 1):
                first, second = second, max(first + nums[i], second)
            return second
        
        length = len(nums)
        if length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0], nums[1])
        else:
            return max(robRange(0, length - 2), robRange(1, length - 1))

# C++
# 如果不偷窃最后一间房屋，则偷窃房屋的下标范围是 [0, n-2]；
# 如果不偷窃第一间房屋，则偷窃房屋的下标范围是 [1, n-1]。
# 对于两段下标范围分别计算可以偷窃到的最高总金额。
# 使用滚动数组，在每个时刻只需要存储前两间房屋的最高总金额。
class Solution {
public:
    int robRange(vector<int>& nums, int start, int end) {
        int first = nums[start], second = max(nums[start], nums[start + 1]);
        for (int i = start + 2; i <= end; i++) {
            int temp = second;
            second = max(first + nums[i], second);
            first = temp;
        }
        return second;
    }
    int rob(vector<int>& nums) {
       int length = nums.size();
       if (length == 1) {
           return nums[0];
       } else if (length == 2) {
           return max(nums[0], nums[1]);
       }
       return max(robRange(nums, 0, length - 2), robRange(nums, 1, length - 1));
    }
};