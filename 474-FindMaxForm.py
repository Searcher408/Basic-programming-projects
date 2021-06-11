# Python3
from typing import List

# 三维 dp
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)
        dp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(length + 1)]
        for i in range(1, length + 1):
            zeros = strs[i - 1].count('0')
            ones = strs[i - 1].count('1')
            for j in range(m + 1):
                for k in range(n + 1):
                    dp[i][j][k] = dp[i - 1][j][k]
                    if j >= zeros and k >= ones:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - zeros][k - zeros] + 1)
            return dp[length][m][n]

# 二维 dp
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for str in strs:
            zeros = str.count('0')
            ones = str.count('1')
            for j in range(m, zeros - 1, -1): # 倒序，从 m 到 zeros
                for k in range(n, ones - 1, -1): # 从 n 到 ones
                    dp[j][k] = max(dp[j][k], dp[j - zeros][k - ones] + 1)
        return dp[m][n]

# 动态规划
# 与经典的背包问题相似，经典的背包问题只有一种容量不同，这道题有两种容量，即选取的字符串子集中的 0 和 1 的数量上限。
# 经典的背包问题可以使用二维动态规划求解，两个维度分别是物品和容量。
# 这道题有两种容量，因此需要使用三维动态规划求解，三个维度分别是字符串、0 的容量和 1 的容量。
# 定义三维数组 dp，其中 dp[i][j][k] 表示在前 i 个字符串中，使用 j 个 0 和 k 个 1 的情况下最多可以得到的字符串数量。
# 假设数组 str 的长度为 l，则最终答案为 dp[l][m][n]。

# C++ 空间复杂度为 O(lmn) 
class Solution {
public:
    vector<int> getZerosOnes(string& str) {
        vector<int> zerosOnes(2);
        int length = str.length();
        for (int i = 0; i < length; i++) {
            zerosOnes[str[i] - '0']++;
        }
        return zerosOnes;
    }

    int findMaxForm(vector<string>& strs, int m, int n) {
        int length = strs.size();
        // dp[l+1][m+1][n+1]
        vector<vector<vecto<int>>> dp(length + 1, vector<vector<int>>(m + 1， vector<int>(n + 1)));
        // i = 0, 0≤j≤m , 0≤k≤n，dp[i][j][k]=0
        for (int i = 1; i <= length; i++) {
            vector<int>&& zerosOnes = getZerosOnes(strs[i - 1]);
            int zeros = zerosOnes[0], ones = zerosOnes[1];
            for (int j = 0; j <= m; j++) {
                for (int k = 0; k <= n; k++) {
                    dp[i][j][k] = dp[i - 1][j][k];
                    if (j >= zeros && k >= ones) {
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - zeros][k - ones] + 1);
                    }
                }
            }
        }
        return dp[length][m][n];
    }
};

# 由于 dp[i][][] 的每个元素值的计算只和 dp[i−1][][] 的元素值有关，因此可以使用滚动数组的方式去掉 dp 的第一个维度，
# 将空间复杂度优化到 O(mn)。实现时，内层循环需采用倒序遍历的方式，这种方式保证转移来的是 dp[i−1][][] 中的元素值。
# 时间复杂度：O(lmn+L)，其中 l 是数组 strs 的长度，m 和 n 分别是 0 和 1 的容量，L 是数组 strs 中的所有字符串的长度之和。
class Solution {
public:
    vector<int> getZerosOnes(string& str) {
        vector<int> zerosOnes(2);
        int length = str.length();
        for (int i = 0; i < length; i++) {
            zerosOnes[str[i] - '0']++;
        }
        return zerosOnes;
    }

    int findMaxForm(vector<string>& strs, int m, int n) {
        int length = strs.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1));
        for (int i = 0; i < length; i++) {
            vector<int>&& zerosOnes = getZerosOnes(strs[i]);
            int zeros = zerosOnes[0], ones = zerosOnes[1];
            for (int j = m; j >= zeros; j--) { // 更新的时候要用到前面的值，倒序才可以更新的时候不影响下一个值更新。
                for (int k = n; k >= ones; k--) {
                    dp[j][k] = max(dp[j][k], dp[j - zeros][k - ones] + 1);
                }
            }
        }
        return dp[m][n];
    }
};

# int&&可以理解为右值引用，其作用是将变量绑定到一个临时变量上，一般是函数返回值。
# int&& a = some_method();
# 这样可以减少函数返回并且赋值操作时new、delete、copy操作，提高效率。特别是当返回类型比较庞大的时候，作用明显。
# int&&作为形参的情况，作用类似。

# 一个表达式是左值还是右值，取决于使用的是它的值还是它在内存中的位置（作为对象的身份）。
# 也就是说一个表达式具体是左值还是右值，要根据实际在语句中的含义来确定。
# int foo(42);
# int bar;
# bar = foo;
# 将 foo 的值赋给 bar，保存在 bar 对应的内存中；foo 在这里作为表达式是右值；bar 在这里作为表达式是左值。但是 foo 作为对象，既可以充当左值又可以充当右值。

# 在 C++ 中，有两种对对象的引用：左值引用和右值引用。右值引用主要用于移动语义和完美转发。
# 左值引用是常见的引用，所以一般在提到「对象的引用」的时候，指得就是左值引用。将一个对象的内存空间绑定到另一个变量上，那么这个变量就是左值引用。
# 在建立引用的时候是「将内存空间绑定」，因此使用的是一个对象在内存中的位置，这是一个左值。因此不能将一个右值绑定到左值引用上。
# 另一方面，由于常量左值引用保证了不能通过引用改变对应内存空间的值，因此可以将右值绑定在常量引用上。
# int foo(42);
# int& bar = foo;  // OK: foo 在此是左值，将它的内存空间与 bar 绑定在一起
# int& baz = 42;   // Err: 42 是右值，不能将它绑定在左值引用上
# const int& qux = 42;  // OK: 42 是右值，但是编译器可以为它开辟一块内存空间，绑定在 qux 上

# 和声明左值引用一样，右值引用也必须立即进行初始化操作，且只能使用右值进行初始化。
# 和常量左值引用不同的是，右值引用还可以对右值进行修改。
# int foo(42);
# int& bar = foo;        // OK: 将 foo 绑定在左值引用上
# int&& baz = foo;       // Err: foo 可以是左值，所以不能将它绑定在右值引用上
# int&& qux = 42;        // OK: 将右值 42 绑定在右值引用上
# int&& quux = foo * 1;  // OK: foo * 1 的结果是一个右值，将它绑定在右值引用上
# int& garply = foo++;   // Err: 后置自增运算符返回的是右值，不能将它绑定在左值引用上
# int&& waldo = foo--;   // OK: 后置自减运算符返回的是右值，将它绑定在右值引用上
# 由于右值引用只能绑定在右值上，而右值要么是字面常量，要么是临时对象，所以：
# 右值引用的对象，是临时的，即将被销毁；并且右值引用的对象，不会在其它地方使用。

# int foo(42);
# int& bar = foo;     // bar 是对 foo 的左值引用
# int& baz = bar;     // baz 是对 bar 的左值引用，因而 bar 是左值
# int qux = ++foo;    // 前置自增运算符返回左值引用，在这里赋值给 qux，此时左值引用作为右值
# 不论是左值引用还是右值引用，都有：当引用作为变量被保存下来，那么它是左值；否则它是右值。

# 浅拷贝：对基本数据类型进行值传递，对引用数据类型进行引用传递般的拷贝，此为浅拷贝。
# 深拷贝：对基本数据类型进行值传递，对引用数据类型，创建一个新的对象，并复制其内容，此为深拷贝。
# 深拷贝拷贝的是内容,浅拷贝拷贝的是指针,判断是深拷贝还是浅拷贝只需要看对象的内存地址是否发生改变。

# 深拷贝的实现过程并不是完全的递归，否则如果对象的某级子元素是它自身的话，这个过程就死循环了。
# 实际上，如果遇到已经处理过的对象，就会直接使用其引用，而不再重复处理。
# from copy import deepcopy
# a = [3, 4]
# m = [1, 2, a, [5, a]]
# n = deepcopy(m)
# n[3][1][0] = -1 
# print(n) # [1, 2, [-1, 4], [5, [-1, 4]]]
# https://zhuanlan.zhihu.com/p/40449219