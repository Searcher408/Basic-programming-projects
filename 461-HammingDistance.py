# Python3
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xList = list()
        yList = list()
        while x:
            xList.append(x%2)
            x = x // 2
        while y:
            yList.append(y%2)
            y = y // 2
        
        cnt = 0
        while xList or yList:
            if xList:
                x = xList.pop(0)
            else:
                x = 0
            
            if yList:
                y = yList.pop(0)
            else:
                y = 0
            
            if x != y:
                cnt += 1
        
        return cnt

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')

# Java
class Solution {
    public int hammingDistance(int x, int y) {
        int cnt = 0;
        if (x == y) {
            return 0;
        }
        while (x!=0 || y!=0) {
            if (x%2 != y%2) {
                cnt++;
            }
            x = x / 2;
            y = y / 2;
        }
        return cnt;
    }
}

# C++
class Solution {
public:
    int hammingDistance(int x, int y) {
        x = x ^ y; // 2^4=6 010^100=110
        y = 0; // 用y来计数
        while (x) {
            if (x % 2) {
                y++;
            }
            x /= 2;
        }
        return y;
    }
};

# 内置位计数功能：大多数编程语言都内置了计算二进制表达中 1 的数量的函数。
class Solution {
public:
    int hammingDistance(int x, int y) {
        return __builtin_popcount(x ^ y);
    }
};

# Brian Kernighan 算法 
# 通过"与"运算跳过两个 1 之间的 0，直接对 1 进行计数
# f(x) 表示 x 和 x-1 进行与运算所得的结果（即 f(x)=x & (x−1)），那么 f(x) 恰为 x 删去其二进制表示中最右侧的 1 的结果。
class Solution {
public:
    int hammingDistance(int x, int y) {
        int s = x ^ y, ret = 0;
        while (s) {
            s &= s - 1;
            ret++;
        }
        return ret;
    }
};

# Python3
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = x ^ y
        y = 0
        while x:
            x &= x - 1
            y += 1
        return y