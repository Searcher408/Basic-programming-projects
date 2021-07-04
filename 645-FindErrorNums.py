# Python3
from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        flag = [0]*n
        for i in nums:
            flag[i - 1] += 1
        a, b = 0, 0
        for j in range(n):
            if flag[j] == 2:
                a = j + 1
            if flag[j] == 0:
                b = j + 1
        return [a, b]

# C 哈希表
struct HashTable {
    int key, val;
    UT_hash_handle hh;
};

int cmp(int *a, int *b) {
    return *a - *b;
}

int* findErrorNums(int* nums, int numsSize, int* returnSize) {
    int* errorNums = malloc(sizeof(int) * 2);
    *returnSize = 2;
    struct HashTable* hashTable = NULL;
    for (int i = 0; i < numsSize; i++) {
        struct HashTable* tmp;
        HASH_FIND_INT(hashTable, &nums[i], tmp);
        if (tmp == NULL) {
            tmp = malloc(sizeof(struct HashTable));
            tmp->key = nums[i], tmp->val = 1;
            HASH_ADD_INT(hashTable, key, tmp);
        } else {
            tmp->val++;
        }
    }
    for (int i = 1; i <= numsSize; i++) {
        struct HashTable* tmp;
        HASH_FIND_INT(hashTable, &i, tmp);
        if (tmp == NULL) {
            errorNums[1] = i;
        } else if (tmp->val == 2) {
            errorNums[0] = i;
        }
    }
    return errorNums;
}

# 数学方法 求和后计算差值
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum_set = sum(set(nums)) #去重后的求和
        tot = ( n * (n + 1) ) >> 1  
        return [sum(nums) - sum_set, tot - sum_set]

# Java 
# 因为值的范围在 [1, n]，运用「桶排序」的思路，根据 nums[i] = i + 1的对应关系使用 O(n)的复杂度将每个数放在其应该落在的位置里。
# 然后线性扫描一遍排好序的数组，找到不符合 nums[i] = i + 1对应关系的位置，从而确定重复元素和缺失元素是哪个值。
class Solution {
    public int[] findErrorNums(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            while (nums[i] != i + 1 && nums[nums[i] - 1] != nums[i]) {
                swap(nums, i, nums[i] - 1);
            }
        }
        int a = -1, b = -1;
        for (int i = 0; i < n; i++) {
            if (nums[i] != i + 1) {
                a = nums[i];
                b = i == 0 ? 1 : nums[i - 1] + 1;
            }
        }
        return new int[]{a, b};
    }
    void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
