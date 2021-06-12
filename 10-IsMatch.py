# Python3
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]
        
        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1): # 0个字符到m个字符
            for j in range(1, n + 1): # 1个字符到n个字符
                if p[j - 1] == '*': # 判断p中第j个字符是否为'*'，在数组中索引为j-1
                    f[i][j] = f[i][j - 2]
                    if matches(i, j - 1): # 判断s中第i个字符与p中第j-1个字符是否匹配
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j): # 判断s中第i个字符与p中第j个字符是否匹配
                        f[i][j] = f[i - 1][j - 1]
        
        return f[m][n]

# 由于大部分语言中，字符串的字符下标是从 0 开始的，因此在实现上面的状态转移方程时，需要注意状态中每一维下标与实际字符下标的对应关系。 
# 循环中i, j表示相应状态，用i, j操作字符数组时需要减去1                    

# 动态规划 时间复杂度 O(mn)，m 和 n 是字符串 s 和 p 的长度。需要计算出所有状态，并且每个状态在进行转移时的时间复杂度为 O(1)。
# 空间复杂度 O(mn)，即为存储所有状态使用的空间。
# 用 f[i][j] 表示 s 的前 i 个字符与 p 中的前 j 个字符是否能够匹配。
# 动态规划的边界条件为 f[0][0]=true，即两个空字符串是可以匹配的。最终的答案即为 f[m][n]。
# C++ 
class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size();
        int n = p.size();

        auto matches = [&](int i, int j) { // C++11中的匿名函数(lambda函数,lambda表达式)
            if (i == 0) {
                return false; 
            }
            if (p[j - 1] == '.') {
                return true;
            }
            return s[i - 1] == p[j - 1];
        };// 隐式返回类型
        // [&] 用到的任何外部变量都隐式按引用捕获

        vector<vector<int>> f(m + 1, vector<int>(n + 1));
        f[0][0] = true;
        for (int i = 0; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p[j - 1] == '*') {
                    f[i][j] = f[i][j-2];
                    if (matches(i, j - 1)) {
                        f[i][j] |= f[i - 1][j];
                    }
                } else {
                    if (matches(i, j)) {
                        f[i][j] = f[i-1][j-1];
                    }
                }
            }
        }

        return f[m][n];
    }
};

# Java
class Solution {
    public boolean isMatch(String s, String p) {
        int m = s.length();
        int n = p.length();

        boolean[][] f = new boolean[m + 1][n + 1];
        f[0][0] = true;
        for (int i = 0; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p.charAt(j - 1) == '*') {
                    f[i][j] = f[i][j - 2];
                    if (matches(s, p, i, j - 1)) {
                        f[i][j] = f[i][j] || f[i - 1][j];
                    }
                } else {
                    if (matches(s, p, i, j)) {
                        f[i][j] = f[i - 1][j - 1];
                    }
                }
            }
        }
        return f[m][n];
    }

    public boolean matches(String s, String p, int i, int j) {
        if (i == 0) {
            return false;
        }
        if (p.charAt(j - 1) == '.') {
            return true;
        }
        return s.charAt(i - 1) == p.charAt(j - 1);
    }
}

'''
以一个例子详解动态规划转移方程：
S = abbbbc
P = ab*d*c
1. 当 j 指向的字符为字母（'.' 可以看成一个可以匹配任何字母的特殊字母）时，
   只需判断对应位置的字符即可，
   若相等，还需判断 i,j 之前的字符串是否匹配，转化为f[i][j] = f[i-1][j-1].
   若不等，则 f[i][j] = false.
   
       f[i-1][j-1]   i
            |        |
   S [a  b  b  b  b][c] 
   
   P [a  b  *  d  *][c]
                     |
                     j
   

2. 如果当前 j 指向的字符为 '*'，则把类似 'a*', 'b*' 等当成整体看待。
   首先选择让 'b*' 不进行匹配，f[i][j] = f[i][j-2]:

            i
            |
   S  a  b [b] b  b  c  
    
   P [a] b  *  d  *  c
      |
      j <--

   接着开始判断是否能够匹配 'b*'

            i
            |
   S  a  b [b] b  b  c  
   
   P  a [b  *] d  *  c
            |
            j
   
   注意到当 'b*' 匹配完 'b' 之后，它仍然可以继续发挥作用。
   因此可以只把 i 前移一位，而不丢弃 'b*', 转化为f[i][j] = f[i-1][j]:
   
         i
         | <--
   S  a [b] b  b  b  c  
   
   P  a [b  *] d  *  c
            |
            j

3. 在状态转移方程中，如果字符串 p 中包含一个「字符 + 星号」的组合（例如 b*），
   那么在进行状态转移时，会先将 b 进行匹配（当 p[j] 为 b 时），再将 b* 作为整体进行匹配（当 p[j] 为 * 时）。
   额外的状态转移不会影响答案，因为当 j 指向 'b*' 中的 'b' 时, 所得状态f[i][j] = f[i-1][j-1],
   由于当循环到下一步 j 指向 '*' 时(此时i未变化), 首先预设'b*'不匹配时得到状态f[i][j] = f[i][j-2], 
   后续判断'b*'中的'b'若能够匹配后才会更新f[i][j] = f[i-1][j]，过程中没有用到上一步j-1指向'b'的状态f[i][j-1]。
'''