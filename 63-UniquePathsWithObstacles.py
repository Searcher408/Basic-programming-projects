# Python3 动态规划
# 用 f(i, j) 来表示从坐标 (0, 0) 到坐标 (i, j) 的路径总数，
# u(i, j) 表示坐标 (i, j) 是否可行， 如果坐标 (i, j) 有障碍物，u(i, j) = 0, 否则 u(i, j) = 1
# 从坐标 (0, 0) 到坐标 (i, j) 的路径总数的值只取决于从坐标 (0, 0) 到坐标 (i-1, j) 的路径总数和
# 从坐标 (0, 0) 到坐标 (i, j-1) 的路径总数，即 f(i, j) 只能通过 f(i-1 , j) 和 f(i, j-1) 转移得到
# 当坐标 (i, j) 本身有障碍的时候，任何路径都到不了 f(i, j), 此时 f(i, j) = 0
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [0] * m

        dp[0] = int(obstacleGrid[0][0] == 0)
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                    continue
                if j-1 >= 0 and obstacleGrid[i][j-1] == 0:
                    dp[j] += dp[j-1]
        return dp[-1]
        
# (i, j) 位置只能从 (i-1, j) 和 (i, j-1) 走到，这样的条件说明状态转移是 【无后效性】的
# 动态规划的题目分为两大类，一种是求最优解类，典型问题是背包问题，另一种就是计数类，比如这里的统计方案数
# 的问题，它们都存在一定的递推性质。前者的递推性质还有一个名字叫做【最优子结构】--即当前问题的最优解取决于子
# 问题的最优解，后者类似，当前问题的方案数取决于子问题的方案数。所以在遇到求方案数的问题时，可以往动态规划
# 的方向考虑
# C++ 时间复杂度O(mn) 空间复杂度O(m) 利用滚动数组优化
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int n = obstacleGrid.size(), m = obstacleGrid.at(0).size();

        vector<int> f(m); //滚动数组

        f[0] = (obstacleGrid[0][0] == 0);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (obstacleGrid[i][j] == 1) {
                    f[j] = 0;
                    continue;
                }
                if (j-1 >= 0 && obstacleGrid[i][j-1] == 0) {
                    f[j] += f[j-1];
                }
            }
        }

        return f.back();
    }
}