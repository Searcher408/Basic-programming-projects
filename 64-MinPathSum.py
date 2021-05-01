# Python3
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # if m == 1 and n == 1:
        #     return grid[0][0]
        
        dp = [0]*n
           
        for i in range(m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                if i == 0:
                    dp[j] = dp[j-1] + grid[0][j]
                else:
                    dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
        return dp[n-1]

def main():
    test = Solution()
    grid = [[9,1,4,8]]
    res = test.minPathSum(grid)
    print(res)

if __name__ == "__main__":
    main()

# 动态规划 时间复杂度O(mn) 空间复杂度O(mn), 可优化至O(n)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, columns = len(grid), len(grid[0])
        dp = [[0] * columns for _ in range(rows)]
        dp[0][0] = grid[0][0]

        for i in range(1, rows):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, columns):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, rows):
            for j in range(1, columns):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[rows-1][columns-1]
