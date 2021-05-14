# Python3
class Solution:
    
    def romanToInt(self, s: str) -> int:
        roman_digits = {'M':1000, 'CM':900, 'D':500, 'CD':400, 
                    'C':100, 'XC':90, 'L':50, 'XL':40,
                    'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
        
        s = s + ' ' # 防止字符串遍历越界，末尾加上空字符
        res = 0
        i = 0
        while i < len(s)-1:
            if s[i] == "C" and s[i+1] == "M":
                res += roman_digits['CM']
                i = i + 2
            elif s[i] == "C" and s[i+1] == "D":
                res += roman_digits['CD']
                i = i + 2
            elif s[i] == "X" and s[i+1] == "C":
                res += roman_digits["XC"]
                i = i + 2
            elif s[i] == "X" and s[i+1] == "L":
                res += roman_digits['XL']
                i = i + 2
            elif s[i] == "I" and s[i+1] == "X":
                res += roman_digits['IX']
                i = i + 2
            elif s[i] == "I" and s[i+1] == "V":
                res += roman_digits['IV']
                i = i + 2
            else:
                tmp = s[i]
                res += roman_digits[tmp]
                i = i + 1
        
        return res

def main():
    test = Solution()
    s = "MCMXCIV"
    res = test.romanToInt(s)
    print(res)

if __name__ == "__main__":
    main()

# Python
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 
            'XC':80, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}
        
        return sum( d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s) )
        # get(key, default) 函数可以通过 key 从 d 中找出对应的值，如果 key 不存在则返回默认值 default
        # 例如 'II'不是key，则返回d['I'] = 1
# 举个例子，遍历经过 IV 的时候先记录 I 的对应值 1 再往前移动一步记录 IV 的值 3，
# 加起来正好是 IV 的真实值 4。max 函数在这里是为了防止遍历第一个字符的时候出现 [-1:0] 的情况

# C++ 
class Solution {
public:
    int romanToInt(string s) {
        unordered_map<string, int> m = {{"I", 1}, {"IV", 3}, {"IX", 8}, {"V", 5}, {"X", 10}, {"XL", 30}, {"XC", 80}, 
                                        {"L", 50}, {"C", 100}, {"CD", 300}, {"CM", 800}, {"D", 500}, {"M", 1000}};
        int r = m[s.substr(0, 1)];
        for (int i = 1; i < s.size(); i++) { # 从s[1]开始遍历，防止出现s[-1]
            # substr函数的形式为s.substr(pos, n)，需要两个参数，第一个是开始位置，第二个是获取子串的长度。
            string two = s.substr(i-1, 2);
            string one = s.substr(i, 1);
            r += m[two] ? m[two] : m[one];
        }
        return r;
    }
};
# 关联式容器的底层实现采用的树存储结构，更确切的说是红黑树结构；(map、multimap、set、multiset)
# 无序容器（哈希容器）的底层实现采用的是哈希表的存储结构。(unordered_map、unordered_multimap、unordered_set、unordered_multiset)
# 和关联式容器相比，无序容器具有以下 2 个特点：
# 1.无序容器内部存储的键值对是无序的，各键值对的存储位置取决于该键值对中的键，
# 2.和关联式容器相比，无序容器擅长通过指定键查找对应的值（平均时间复杂度为 O(1)）；
# 但对于使用迭代器遍历容器中存储的元素，无序容器的执行效率则不如关联式容器。