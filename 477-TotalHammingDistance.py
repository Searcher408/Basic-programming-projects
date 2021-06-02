# Python3
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i, n):
                res += bin(nums[i] ^ nums[j]).count(1)
        return res

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i, n):
                s = nums[i] ^ nums[j]
                while s:
                    s &= s - 1
                    res += 1
        return res

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        # 10 ^ 9 = (10 ^ 3) ^ 3 < (2 ^ 10) ^ 3 = 2 ^ 30 (x位2进制 可以表示的原码最大值为 2^x-1)
        # 由于数组中最大值为1e9,也就是说用30位二进制就能表示最大值。
        for i in range(30):
            c = sum( (val >> i) & 1 for val in nums)
            ans += c * (n - c)

        return ans

# 对于整数 val 二进制的第 i 位，可以用代码 (val >> i) & 1 来取出其第 i 位的值。
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        return sum((j:=sum(num>>i&1 for num in nums))*(len(nums)-j) for i in range(30))

# PEP572建议支持Python中的:=运算符，以允许在表达式中进行变量赋值。此语法在Python 3.8中提供。
# https://www.thinbug.com/q/26000198