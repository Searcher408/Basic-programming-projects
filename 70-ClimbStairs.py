# Python3
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        i = 1
        j = 2
        while n > 2:     
            j = j + i
            i = j - i
            n = n - 1
        return j

# C++ 动态规划 时间复杂度为 O(n) 空间复杂度为 O(1)
class Solution {
public:
    int climbStairs(int n) {
        int p = 0, q = 0, r = 1;
        for (int i = 1; i <=n; i++) {
            p = q;
            q = r;
            r = p + q;
        }
        return r;
    }
};

# 矩阵快速幂 时间复杂度同快速幂O(logn) 空间复杂度O(1)
# 递归式为齐次线性递推式，则可以把数列的递推关系转化为
# 矩阵的递推关系，即构造出一个矩阵的 n 次方乘以一个列
# 向量得到一个列向量，这个列向量中包含我们要求的 f(n)
class Solution {
public:
    vector<vector<long long>> multiply(vector<vector<long long>> &a, vector<vector<long long>> &b) {
        vector<vector<long long>> c(2, vectoc<long long>(2));
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j];
            }
        }
        return c;
    }

    vector<vector<long long>> matrixPow(vector<vector<long long>> a, int n) {
        vector<vector<long long>> ret = {{1,0},{0,1}};
        while (n > 0) {
            if ((n & 1) == 1) { # n减半至1时为真
                ret = multiply(ret, a);
            }
            n >>= 1; # n每次右移减半，加速计算
            a = multiply(a, a);
        }
        return ret;
    }

    int climbStairs(int n) {
        vector<vector<long long>> ret = {{1, 1}, {1, 0}};
        vector<vector<long long>> res = matrixPow(ret, n);
        
        return res[0][0];
    }
};

# 通项公式 
# 根据递推方程 f(n) = f(n - 1) + f(n - 2)，
# 可以写出特征方程：x^2 = x + 1, 求出x_1和x_2
# 设通解为 f(n) = c_1 x_1 ^n + c_2 x_2 ^ n
# 代入初始条件 f(1) = 1，f(2) = 1
# 求出c_1和c_2得到通项公式
# 代码中使用的pow 函数的时空复杂度与 CPU 支持的指令集相关
class Solution {
public:
    int climbStairs(int n) {
        double sqrt5 = sqrt(5);
        double fibn = pow((1 + sqrt5) / 2, n + 1) - pow((1 - sqrt5) / 2, n + 1);
        return (int)round(fibn / sqrt5);
    }
};
