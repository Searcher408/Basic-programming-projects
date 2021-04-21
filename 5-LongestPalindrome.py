# Python3 动态规划 时间复杂度O(n^2), 空间复杂度O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        maxLen = 1
        begin = 0

        # dp[i][j] 表示 s[i..j]是否是回文串
        dp = [[False] * n for _ in range(n)] # 创建n*n状态矩阵
        for i in range(n):
            dp[i][i] = True

        # 递推开始   
        for L in range(2, n+1): # 先枚举子串长度
            for i in range(n): # 枚举左边界，左边界的上限设置可以宽松一些
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1 
                if j >= n: # 如果右边界越界，退出当前循环
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                
                # 只要 dp[i][L] == True 成立，就表示子串 s[i..L] 是回文，
                # 此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    begin = i
            
        return s[begin : begin + maxLen]

def main():
    test = Solution()
    str = "ababc"
    res = test.longestPalindrome(str)
    print(res)

if __name__ == "__main__":
    main()

# C++ 动态规划
class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        if (n < 2) {
            return s;
        }

        int maxLen = 1;
        int begin = 0;
        vector<vector<int>> dp(n, vector<int>(n));
        for (int i = 0; i < n; i++) {
            dp[i][i] = true; //初始化：所有长度为1的子串都是回文串
        }

        //递推开始
        for (int L = 2; L <= n; L++) {
            for (int i = 0; i < n; i++) {
                int j = i + L - 1;
                if (j >= n) {
                    break;
                }

                if (s[i] != s[j]) {
                    dp[i][j] = false;
                } else {
                    if (j - i < 3) {
                        dp[i][j] = true;
                    } else {
                        dp[i][j] = dp[i+1][j-1];
                    }
                }

                if (dp[i][j] && j - i + 1 > maxLen) {
                    maxLen = j - i + 1;
                    begin = i;
                }
            }
        }
       
        /*
        string str;
        int k = 0;
        for (int t = begin; t < maxLen; t++) {
            str[k] = s[t];
            k++;
        }
        */

        return  s.substr(begin, maxLen);    
    }
};

//初始化二维数组vector<vector <int> > test(m ,vector<int>(n,0));    
//m*n的二维vector，所有元素为0

# Java 动态规划
public class Solution {
    public String longestPalindrome(String s) {
        int len = s.length();
        if (len < 2) {
            return s;
        }

        int maxLen = 1;
        int begin = 0;
        boolean[][] dp = new boolean[len][len];
        for (int i = 0; i < len; i++) {
            dp[i][i] = true;
        }

        char[] charArray = s.toCharArray(); //转换为字符数组
        for (int L = 2; L <= len; L++) {
            for (int i = 0; i < len; i++) {
                int j = i + L - 1;
                if (j >= len) {
                    break;
                }

                if (charArray[i] != charArray[j]) {
                    dp[i][j] = false;
                } else {
                    if (j - i < 3) {
                        dp[i][j] = true;
                    } else {
                        dp[i][j] = dp[i + 1][j - 1];
                    }
                }

                if (dp[i][j] && j - i + 1 > maxLen) {
                    maxLen = j - i + 1;
                    begin = i;
                }
            }
        }
        return s.substring(begin, maxLen);
    }
}

