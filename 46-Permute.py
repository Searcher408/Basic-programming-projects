# Python3
from typing import List

# 回溯
# 将题目给定的 n 个数的数组 nums 划分成左右两个部分，左边的表示已经填过的数，右边表示待填的数，在回溯的时候动态维护这个数组。
# 假设已经填到第first 个位置，那么nums 数组中[0,first−1] 是已填过的数的集合，[first,n−1] 是待填的数的集合。
# 尝试用[first,n−1] 里的数去填第first 个数，假设待填的数的下标为 i ，那么填完以后将第 i 个数和第first 个数交换，
# 即能使得在填第first+1个数的时候nums 数组的[0,first] 部分为已填过的数，[first+1,n−1] 为待填的数，
# 回溯的时候交换回来即能完成撤销操作。这样生成的全排列并不是按字典序存储在答案数组中的，
# 如果题目要求按字典序输出，那么请还是用标记数组或者其他方法。
# 时间复杂度：OO(n×n!)，其中 n 为序列的长度。空间复杂度：O(n)，除答案数组以外，递归函数在递归过程中需要为每一层递归函数分配栈空间，
# 所以这里需要额外的空间且该空间取决于递归的深度，这里可知递归调用深度为 O(n)。
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0):
            if first == n: # 所有数都填完了
                res.append(nums[:])

            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first] # 动态维护数组
                backtrack(first + 1) # 继续递归填入下一个数
                nums[first], nums[i] = nums[i], nums[first] # 撤销操作
        
        n = len(nums)
        res = list()
        backtrack()
        return res


if __name__ == "__main__":
    test = Solution()
    nums = [1,2,3]
    res = test.permute(nums)
    print(res)

# C++
class Solution {
public:
    void backtrack(vector<vector<int>>& res, vector<int>& output, int first, int len) {
        if (first == len) {
            res.emplace_back(output);
            return;
        }

        for (int i = first; i < len; i++) {
            swap(output[i], output[first]);
            backtrack(res, output, first + 1, len);
            swap(output[i], output[first]);
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        backtrack(res, nums, 0, (int)nums.size());
        return res;
    }
};