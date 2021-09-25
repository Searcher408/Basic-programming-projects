# Python3
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        lcs = dp[m][n]
        return m - lcs + n - lcs

# C++ 最长公共子序列 时间复杂度：O(mn)
class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1));

        for (int i = 1; i <= m; i++) {
            char c1 = word1[i - 1];
            for (int j = 1; j <= n; j++) {
                char c2 = word2[j - 1];
                if (c1 == c2) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }

        return m + n - dp[m][n] * 2;
    }
};

class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.length(), n = word2.length();
        if (m == 0 || n == 0) {
            return m + n;
        }
        vector<vector<int>> dp( m+ 1, vector<int>(n + 1, 0));
        for (int i = 1; i <= m; i++) {
            if (word1[i - 1] == word2[0]) {
                while (i <= m) {
                    dp[i][1] = 1;
                    i++;
                }
            }
        }
        for (int j = 1; j <= n; j++) {
            if (word1[0] == word2[j - 1]) {
                while (j <= n) {
                    dp[1][j] = 1;
                    j++;
                }
            }
        }

        for (int i = 2; i <= m; i++) {
            for (int j = 2; j <= n; j++) {
                if (word1[i - 1] == word2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]);
                }
            }
        }

        // for (int i = 0; i <= m; i++) {
        //     for (int j = 0; j <= n; j++) {
        //         std::cout << dp[i][j] << ' ';
        //     }
        //     std::cout << std::endl;
        // }
        return m + n - dp[m][n] * 2;
    }
};

# C++ 直接使用动态规划计算最少删除操作次数，不需要计算最长公共子序列的长度。
# dp[i][j] 表示使 word1[0:i] 和 word2[0:j] 相同的最少删除操作次数。
class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1));

        for (int i = 1; i <= m; ++i) {
            dp[i][0] = i;
        }
        for (int j = 1; j <= n; ++j) {
            dp[0][j] = j;
        }
        for (int i = 1; i <= m; i++) {
            char c1 = word1[i - 1];
            for (int j = 1; j <= n; j++) {
                char c2 = word2[j - 1];
                if (c1 == c2) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1;
                }
            }
        }

        return dp[m][n];
    }
};
