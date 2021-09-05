# Python3

# 状态压缩
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        a, b = 0, 1
        res = 0
        while n > 1:
            res = a + b
            a = b
            b = res
            n -= 1
        return res

# 带备忘录的递归解法，自顶向下，时间复杂度是 O(n)
class Solution:
    def fib(self, n: int) -> int:
        def helper(res, n):
            if n == 1 or n == 2:
                return 1
            if res[n] == 0:
                res[n] = helper(res, n-1) + helper(res, n-2)
            return res[n]

        if n < 1:
            return 0
        else:
            res = [0]*(n+1)
            return helper(res, n)

# 动态规划，DPtable, 自底向上，时间复杂度是 O(n)
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        res = [0]*(n+1)
        res[0] = 0
        res[1] = res[2] = 1
        for i in range(3, n+1):
            res[i] = res[i-1] + res[i-2]
        return res[n]