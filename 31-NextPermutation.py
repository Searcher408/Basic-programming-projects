# Python3 两遍扫描
from typing import List

# 以排列 [4,5,2,6,3,1] 为例：
# 找到符合条件的一对「较小数」与「较大数」的组合为 2 与 3，满足「较小数」尽量靠右，而「较大数」尽可能小。
# 完成交换后排列变为 [4,5,3,6,2,1]，此时重排「较大数」右边的序列，序列变为 [4,5,3,1,2,6]。

# 对于长度为 n 的排列 a：
# 1.首先从后向前查找第一个顺序对 (i,i+1)，满足 a[i] < a[i+1]。这样「较小数」即为 a[i]。此时[i+1,n) 必然是下降序列。
# 2.如果找到了顺序对，那么在区间 [i+1,n) 中从后向前查找第一个元素 j 满足 a[i]<a[j]。这样「较大数」即为 a[j]。
# 3.交换 a[i] 与 a[j]，此时区间 [i+1,n) 必为降序。直接使用双指针反转区间 [i+1,n) 使其变为升序，而无需对该区间进行排序。
# 注意：如果在步骤 1 找不到顺序对，说明当前序列已经是一个降序序列，即最大的序列，
# 直接跳过步骤 2 执行步骤 3，即可得到最小的升序序列。该方法支持序列中存在重复元素。

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0: # 已找到a[i]
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]: # 寻找a[j]
                j -= 1
            nums[i], nums[j] = nums[j], nums[i] # 交换
        
        left, right = i + 1, len(nums) - 1 # 反转[i+1, n)
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

# C
void nextPermutation(int *nums, int numsSize) {
    int i = numsSize - 2;
    while (i >= 0 && nums[i] >= nums[i + 1]) {
        i--;
    }
    if (i >= 0) {
        int j = numsSize - 1;
        while (j >= 0 && nums[i] >= nums[j]) {
            j--;
        }
        swap(nums + i, nums + j);
    }
    reverse(nums, i + 1, numsSize - 1);
}

void swap(int *a, int *b) {
    int t = *a;
    *a = *b;
    *b = t;
}

void reverse(int *nums, int left, int right) {
    while (left < right) {
        swap(nums + left, nums + right);
        left++;
        right--;
    }
}
