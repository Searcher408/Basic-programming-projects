# Python3 
class Solution:
    def reverse(self, x:int) -> int:
        flag = False
        if x < 0:
            x = - x
            flag = True
        
        res = 0
        while x:
            res = res * 10 + x % 10
            x = x // 10

        if res > 2**31 - 1:
            res = 0

        if flag:
            res = -res
        
        return res

def main():
    test = Solution()
    ans = test.reverse(-123)
    print(ans)

if __name__ == "__main__":
    main()

# -2^31 <= x <= 2^31 - 1
# C++ 检查是否溢出 时间复杂度O(log(x))，空间复杂度O(1)
class Solution {
public:
    int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;

            if (rev > INT_MAX/10 || (rev == INT_MAX/10 && pop > 7)) {
                return 0;
            }
            if (rev > INT_MAX/10 || (rev == INT_MAX/10 && pop < -8)) {
                return 0;
            }

            rev = rev * 10 + pop;
        }
        return rev;
    }
};

# Java
public int reverse(int x) {
    int ans = 0;
    while (x != 0) {
        if ((ans * 10) / 10 != ans) {
            ans = 0;
            break;
        }
        ans = ans * 10 + x % 10;
        x = x / 10;
    }
    return ans;
}