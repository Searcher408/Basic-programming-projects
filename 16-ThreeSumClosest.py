# Python 3
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = 10**7

        # 根据差值的绝对值来更新答案
        def update(cur):
            nonlocal best # nonlocal关键字：声明此变量与外层同名变量为相同变量
            if abs(cur - target) < abs(best - target):
                best = cur
        
        # a + b + c 接近 target
        # 枚举 a
        for i in range(n):
            # 保证和上一次枚举的元素不相等
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 使用双指针枚举 b 和 c
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]

                # 如果和为 target 则直接返回答案
                if s == target:
                    return target
                update(s)

                if s > target:
                    # 如果a+b+c和大于 target, 左移 c 对应的指针
                    k0 = k - 1
                    # 移动到下一个不相等的元素
                    while j < k0 and nums[k0] == nums[k]:
                        k0 -= 1
                    k = k0
                else:
                    # 如何a+b+c和小于 target, 右移 b 对应的指针
                    j0 = j + 1
                    # 移动到下一个不相等的元素
                    while j0 < k and nums[j0] == nums[j]:
                        j0 += 1
                    j = j0
        
        return best
