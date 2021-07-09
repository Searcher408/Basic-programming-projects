# Python3 双指针
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = slow = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

# C
int removeElement(int* nums, int numsSize, int val) {
    int fast = 0, slow = 0;
    while (fast < numsSize) {
        if (nums[fast] != val) {
            nums[slow++] = nums[fast];
        }
        fast++;
    }
    return slow;
}

int removeElement(int* nums, int numsSize, int val) {
    int slow = 0;
    for (int fast = 0; fast < numsSize; fast++) {
        if (nums[fast] != val) {
            nums[slow] = nums[fast];
            slow++;
        }
    }
    return slow;
}

# C 双指针优化 题目中说「元素的顺序可以改变」
# 避免需要保留的元素的重复赋值操作
int removeElement(int* nums, int numsSize, int val) {
    int left = 0, right = numsSize;
    while (left < right) {
        if (nums[left] == val) {
            nums[left] = nums[right - 1];
            right--;
        } else {
            left++;
        }
    }
    return left;
}