# Python3 
class Solution:
    def isPalindrome(self, x:int) -> bool:
        if x < 0:
            return False
        
        tmp = []
        while x:
            tmp.append(x%10)
            x = x // 10
            print(x)

        print(tmp)
        flag = True
        while len(tmp) > 1: # len(tmp) == 1 也是回文数字
            if tmp[0] == tmp[-1]:
                tmp.remove(tmp[0]) # 删除第一个元素
                tmp.pop() # 删除最后一个元素
                print(tmp)
                continue
            flag = False
            break

        return flag

def main():
    test = Solution()
    x = 10
    res = test.isPalindrome(x)
    print(res)

if __name__ == "__main__":
    main()

# 将数字本身反转，然后将反转后的数字与原始数字进行比较，如果它们是相同的，那么这个数字就是回文。
# 但是，如果反转后的数字大于int.MAX，将遇到整数溢出问题。为了避免数字反转可能导致的溢出问题，
# 考虑只反转 int 数字的一半，如果该数字是回文，其后半部分反转后应该与原始数字的前半部分相同。
# 当原始数字小于或等于反转后的数字时，就意味着我们已经处理了一半位数的数字了。
# x 数字长度为奇数，原始数字小于反转后的数字；x 长度为偶数时相等
# 时间复杂度 O(logn) 空间复杂度O(1)

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0 || (x > 0 && x % 10 == 0)) {
            return false;
        }

        int revertedNumber = 0;
        while (x > revertedNumber) { # x <= revertedNumber
            revertedNumber = revertedNumber * 10 + x % 10;
            x /= 10;
        }
        
        # 当数字长度为奇数时，我们可以通过 revertedNumber/10 去除处于中位的数字。
        return x == revertedNumber || x == revertedNumber / 10;
    }
};
