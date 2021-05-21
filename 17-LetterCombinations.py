# Python 3
from typing import List

# 回溯
# 首先使用哈希表存储每个数字对应的所有可能的字母，然后进行回溯操作
# 回溯过程中维护一个字符串，表示已有的字母排列（如果未遍历完电话号码的所有数字，则已有的字母排列是不完整的）。
# 该字符串初始为空。每次取电话号码的一位数字，从哈希表中获得该数字对应的所有可能的字母，
# 并将其中的一个字母插入到已有的字母排列后面，然后继续处理电话号码的后一位数字，
# 直到处理完电话号码中的所有数字，即得到一个完整的字母排列。然后进行回退操作，遍历其余的字母排列。

# 回溯算法用于寻找所有的可行解，如果发现一个解不可行，则会舍弃不可行的解。
# 在这道题中，由于每个数字对应的每个字母都可能进入字母组合，因此不存在不可行的解，直接穷举所有的解即可。

# 时间复杂度：O(3^m × 4^n)，
# 其中 m 是输入中对应 3 个字母的数字个数（包括数字 2、3、4、5、6、8），
# n 是输入中对应 4 个字母的数字个数（包括数字 7、9），m+n 是输入数字的总个数。
# 当输入包含 m 个对应 3 个字母的数字和 n 个对应 4 个字母的数字时，不同的字母组合一共有 3^m × 4^n种，需要遍历每一种字母组合。

# 空间复杂度：O(m+n) 除了返回值以外，空间复杂度主要取决于哈希表以及回溯过程中的递归调用层数，
# 哈希表的大小与输入无关，可以看成常数，递归调用层数最大为 m+n。

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
  
        def backtrack(index: int):
            if index == len(digits):
                res.append("".join(s))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    s.append(letter)
                    backtrack(index + 1)
                    s.pop()
        
        res = list()
        s = list() # 回溯过程中维护一个字符串表示已有的字母排列
        backtrack(0)
        return res

def main():
    test = Solution()
    digits = "23"
    res = test.letterCombinations(digits)
    print(res)

if __name__ == "__main__":
    main()

# Java 完整示例
# package leetcode._17

# import java.util.ArrayList;
# import Java.util.List;

# public class Solution17 {

#     private String letterMap[] = {
#         " ",    //0
#         "",     //1
#         "abc",  //2
#         "def",  //3
#         "ghi",  //4
#         "jkl",  //5
#         "mno",  //6
#         "pqrs", //7
#         "tuv",  //8
#         "wxyz"  //9
#     };

#     private ArrayList<String> res;

#     public List<String> letterCombinations(String digis) {
#         res = new ArrayList<String>();
#         if (digits.equal("")) {
#             return res;
#         }

#         findCombination(digits, 0, "");
#         return res;
#     }

#     private void findCombination(String digits, int index, String s) {
#         if (index == digits.length()) {
#             res.add(s);
#             return;
#         }

#         Character c = digits.charAt(index);
#         String letters = letterMap[c - '0'];
#         for (int i = 0; i < letters.length(); i++) {
#             findCombination(digits, index+1, s+letters.charAt(i));
#         }

#         return;
#     }
# }

# 当题目中出现 “所有组合” 等类似字眼时就要想到用回溯。

# 定义函数 backtrack(combination, nextdigit)，
# 当 nextdigit 非空时，对于 nextdigit[0] 中的每一个字母 letter，
# 执行回溯 backtrack(combination + letter,nextdigit[1:]，直
# 至 nextdigit 为空。最后将 combination 加入到结果中。

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(combination, nextdigit):
            if len(nextdigit) == 0:
                res.append(combination)
            else:
                for letter in phoneMap[nextdigit[0]]:
                    backtrack(combination + letter, nextdigit[1:])
        
        res = []
        backtrack("", digits)
        return res

# 使用队列
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        queue = [''] # 初始化队列

        for digit in digits:
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                for letter in phone[ord(digit) - 50]: # asxii值50为数字2
                    queue.append(tmp + letter)
        
        return queue