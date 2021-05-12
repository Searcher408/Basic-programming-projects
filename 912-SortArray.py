# 排序算法
# 稳定性：稳定排序，a在b前面且a=b，排序后a仍然在b前面
# 内外排序：内排序所有操作都在内存中完成；外排序由于数据太大，因此把数据放在磁盘中，通过磁盘和内存的数据传输进行排序

# Python3
class Solution:
    def sortArray(self, nums):
        self.nums = nums
        self.quickSort(0, len(nums)-1)
        return self.nums

    def quickSort(self, left, right):
        ''' 快速排序 时间复杂度为 O(nlogn) '''
        if left >= right:
            return

        cur = self.nums[left] # 每次选择左端点为标杆
        l = left
        r = right
        while r > l:
            while r > l and self.nums[r] >= cur: # 从右向左找第一个比cur小的数，赋值给当前左端点nums[l]
                r -= 1
            self.nums[l] = self.nums[r] 

            while l < r and self.nums[l] <= cur: # 从左向右找第一个比cur大的数，赋值给当前右端点nums[r]
                l += 1
            self.nums[r] = self.nums[l]

        self.nums[l] = cur # 排完序后cur左边数的比cur小，右边数的比cur大
        self.quickSort(left, l-1)
        self.quickSort(l+1, right)

class Solution2: 
    def sortArray(self, nums):
        # self.quickSort(nums, 0, len(nums)-1)
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, left, right): # 超出时间限制
        if left >= right:
            return
        
        cur = nums[left]
        l = left
        r = right

        while l < r:
            while l < r and nums[r] >= cur:
                r -= 1
            nums[l] = nums[r]

            while l < r and nums[l] <= cur:
                l += 1
            nums[r] = nums[l]

        nums[l] = cur
        self.quickSort(nums, left, l-1)
        self.quickSort(nums, l+1, right)
    
    def mergeSort(self, nums, l, r):
        if l == r:
            return
        mid = (l + r) // 2
        self.mergeSort(nums, l, mid)
        self.mergeSort(nums, mid + 1, r)

        tmp = []
        i, j = l, mid + 1
        while i <= mid or j <= r:
            if i > mid or (j <= r and nums[j] < nums[i]):
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1
        nums[l: r + 1] = tmp

# import random

# class Solution:
#     def randomized_partition(self, nums, l, r):
#         pivot = random.randint(l, r)
#         nums[pivot], nums[r] = nums[r], nums[pivot]
#         i = l - 1
#         for j in range(l, r):
#             if nums[j] < nums[r]:
#                 i += 1
#                 nums[j], nums[i] = nums[i], nums[j]
#         i += 1
#         nums[i], nums[r] = nums[r], nums[i]
#         return i

#     def randomized_quicksort(self, nums, l, r):
#         if l >= r:
#             return
#         mid = self.randomized_partition(nums, l, r)
#         self.randomized_quicksort(nums, l, mid - 1)
#         self.randomized_quicksort(nums, mid + 1, r)

#     def sortArray(self, nums):
#         self.randomized_quicksort(nums, 0, len(nums) - 1)
#         return nums

def main():
    test = Solution2()
    nums = [2, 5, 6, 8, 4]
    res = test.sortArray(nums)
    print(res)

if __name__ == "__main__":
    main()