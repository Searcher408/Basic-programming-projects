#Python3
from typing import List

# 自顶向下, 一个递归的 dp 函数
# 「备忘录」大大减小了子问题数目，完全消除了子问题的冗余，所以子问题总数不会超过金额数 n
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = dict()
        def dp(n):
            if n in memo:
                return memo[n]
           
            if n == 0:
                return 0
            if n < 0:
                return -1

            res = float('INF')
            for coin in coins:
                subproblem = dp(n - coin)
                if subproblem == -1:
                    continue
                res = min(res, 1 + subproblem)
            
            memo[n] = res if res != float('INF') else -1
            return memo[n]
        
        return dp(amount)

# 自底向上使用 dp table 来消除重叠子问题
# 因为凑成 amount 金额的硬币数最多只可能等于 amount（全用 1 元面值的硬币），
# 所以初始化为 amount + 1 就相当于初始化为正无穷，便于后续取最小值。
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) # 数组大小为 amount + 1，初始值也为 amount + 1
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i],  dp[i - coin] + 1)

        return dp[amount] if dp[amount] != amount else -1
