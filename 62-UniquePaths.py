# Python3 动态规划 时间复杂度O(mn) 空间复杂度O(mn)
# 用 f(i, j) 表示从左上角走到 (i, j) 的路径数量，其中 i 和 j 的范围分别是 [0, m) 和 [0, n)
# 动态规划转移方程 f(i, j) = f(i-1, j) + f(i, j-1)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]

        for j in range(n):
            dp[0][j] = 1

        for i in range(m):
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[1]*n] + [[1] + [0]*(n-1) for _ in range(m-1)]
        print(f)

        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i-1][j] + f[i][j-1]

        return f[m-1][n-1]

class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        # if m == 1 or n == 1:
        #     return 1
        if m < n:
            tmp = m
            m = n
            n = tmp

        res = [1]*n # 滚动数组，空间复杂度降低至O(min(m,n))

        for i in range(1, m): 
            for j in range(1, n):
                # temp = res[j] # 第 i-1 行
                # res[j] = res[j-1] + temp # 第 i 行
                res[j] = res[j-1] + res[j]
        
        return res[n-1]
        
def main():
    test = Solution2()
    res = test.uniquePaths(3, 7)
    print(res)

if __name__ == "__main__":
    main()
        
# C++ 
# vector<vector<int>> f(m, vector<int>(n));

# Java
# int[][] f = new int[m][n];

# 组合数学
# 从左上角到右下角，需要移动 m+n-2 次 (m-1 + n-1) 
# 其中有 m-1 次向下移动，n-1 次向右移动
# 因此路径总数，等于从 m+n-2 次移动中选择 m-1 次向下移动的方案数
# 即组合数 C(m+n-2)(m-1) = (m+n-2)! / (m-1)!(n-1)! = (m+n-2)(m+n-3)...n / (m-1)(m-2)...1

# Python3
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m+n-2, m-1)

# C++ 时间复杂度O(m) 空间复杂度O(1)
class Solution {
public:
    int uniquePaths(int m, int n) {
        long long ans = 1;
        for (int x = n, y = 1; y < m; x++, y++) {
            ans = ans * x / y; 
        } 
        # y = 1, x = n
        # y = m-1 , x = n + (m-1 - 1) = m + n - 2
        return ans;
    }
};