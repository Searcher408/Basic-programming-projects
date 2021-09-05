# Python3

class Solution:
    def numSquares(self, n: int) -> int:
        nums = list()
        for i in range(1, 101):
            if i**2 > n:
                break
            nums.append(i**2)
        
        dp = [n+1]*(n+1)
        dp[0] = 0
        for i in range(n+1):
            for num in nums:
                if i - num < 0:
                    continue
                dp[i] = min(dp[i], dp[i - num] + 1)
              
        return dp[n] if dp[n] != n+1 else -1

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]*(n+1) # 默认初始化值都为0
        for i in range(n+1):
            dp[i] = i # 最坏的情况就是每次+1
            j = 1
            while i - j*j >= 0:
                dp[i] = min(dp[i], dp[i - j*j] + 1)
                j += 1
        return dp[n]