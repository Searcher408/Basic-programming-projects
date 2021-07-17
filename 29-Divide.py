# Python3 倍增法
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            if dividend > -2147483648:
                return -dividend
            return 2147483647 # dividend = -2147483648 = -2^31
        
        sign = 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        dividend = dividend if dividend > 0 else -dividend
        divisor = divisor if divisor > 0 else -divisor

        remain = dividend # 余数
        result = 0 # 商
        while remain >= divisor:
            cur = 1 
            div = divisor 
            while div + div < remain:
                cur += cur # 倍增商
                div += div # 倍增除数
            remain -= div # 余数递减
            result += cur # 商累加

        if sign == -1:
            result = -result
        
        if result > 2147483647:
            result = 2147483647

        return result

if __name__ == "__main__":
    test = Solution()
    res = test.divide(7, -3)
    print(res)

# C++
# 被除数和除数均为 32 位有符号整数。除数不为 0。
# 输入都是int类型，也就是32位的，那么绝对值最大的情况也就是-2^31，
# 环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。
# 本题中，如果除法结果溢出，则返回 2^31 − 1。
class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend == 0) return 0; // 被除数为0
        if (divisor == 1) return dividend; // 除数为1
        if (divisor == -1) {
            if (dividend > INT_MIN) return -dividend;
            return INT_MAX;
        }

        long a = dividend;
        long b = divisor;
        int sign = 1;
        if ((a > 0 && b < 0) || (a < 0 && b > 0)) {
            sign = -1;
        }
        a = a > 0 ? a : -a;
        b = b > 0 ? b : -b;
        long res = div(a, b);
        if (sign > 0) {
            return res > INT_MAX ? INT_MAX : res;
        } 
        return -res;
    }

    // 递归
    // 60/8 = (60-32)/8 + 4 = (60-32-16)/8 + 2 + 4 = (60-32-16-8)/8 + 1 + 2 + 4 = 0 + 1 + 2 + 4 = 7
    int div(long a, long b) { 
        if (a < b) return 0;
        long count = 1;
        long tb = b; // long 防止 tb + tb 溢出
        while ((tb + tb) <= a) {
            count = count + count; 
            tb = tb + tb;
        }
        return div(a - tb, b) + count;
    }
};

