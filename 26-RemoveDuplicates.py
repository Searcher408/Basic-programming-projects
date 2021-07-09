# Python3 双指针
from typing import List

# 定义两个指针 fast 和 slow 分别为快指针和慢指针，快指针表示遍历数组到达的下标位置，
# 慢指针表示下一个不同元素要填入的下标位置，初始时两个指针都指向下标 1。
# 假设数组nums的长度为 n。将快指针fast 依次遍历从1 到n−1 的每个位置，
# 对于每个位置，如果nums[fast]=nums[fast−1]，说明nums[fast]和之前的元素都不同，
# 因此将nums[fast] 的值复制到nums[slow]，然后将slow 的值加1，即指向下一个位置。
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow
        
if __name__ == "__main__":
    test = Solution()
    nums = [1,1,2]
    res = test.removeDuplicates(nums)
    print(res)

# C 双指针
int removeDuplicates(int* nums, int numsSize) {
    if (numsSize == 0) {
        return 0;
    }
    int fast = 1, slow = 1;
    while (fast < numsSize) {
        if (nums[fast] != nums[fast - 1]) {
            nums[slow] = nums[fast];
            slow++;
        }
        fast++;
    }
    return slow;
}