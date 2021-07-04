# Python
# 对通项公式进行转换，a_0 - 1是 number−1 除以 26 的余数，从而得到a_0的值。
# 同样地，可以得到a_1到a_n-1的值。时间复杂度即为将 columnNumber 转换成 26 进制的位数。
# 代码实现时，由于计算列名称的顺序是从右往左，因此需要将拼接后的结果反转。
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = list()
        while columnNumber > 0:
            a = (columnNumber - 1) % 26 + 1
            ans.append(chr(a - 1 + ord('A')))
            columnNumber = (columnNumber - a) // 26
        return ''.join(ans[::-1])

if __name__ == "__main__":
    test = Solution()
    num = 52
    res = test.convertToTitle(num)
    print(res)

# C
void reverse(char* str, int strSize) {
    int left = 0, right = strSize - 1;
    while (left < right) {
        char tmp = str[left];
        str[left] = str[right], str[right] = tmp;
        left++;
        right--;
    }
}

char* convertToTitle(int columnNumber) {
    char* ans = malloc(sizeof(char) * 8);
    int ansSize = 0;
    while (columnNumber > 0) {
        int a = (columnNumber - 1) % 26 + 1;
        ans[ansSize++] = a - 1 + 'A';
        columnNumber = (columnNumber - a) / 26;
    }
    ans[ansSize] = '\0';
    reverse(ans, ansSize);
    return ans;
}

# Python 优化
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = list()
        while columnNumber > 0:
            columnNumber -= 1
            ans.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26
        return ''.join(ans[::-1])