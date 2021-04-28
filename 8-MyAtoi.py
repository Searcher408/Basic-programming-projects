# # Python3
# class Solution:
#     def myAtoi(self, s: str) -> int:
#         if len(s) == 0:
#             return 0

#         i = 0 # 索引
#         flag = False # 判断正负数
#         signed = False # 判断正负号是否正常
#         onlyOne = True # 只允许在遍历中出现一次
#         resStr = ""
#         while i < len(s):
#             if onlyOne and s[i] == ' ': # 未考虑"   +0 123"
#                i += 1
#                continue
#             onlyOne = False

#             if s[i] == '+' or s[i] == '-': # 未考虑"+-12" "00000-42a1234"
#                 if signed: # 正负号不正常，超过两个或在数字后出现
#                     break   
#                 if s[i] == '-': 
#                     flag = True   
#                 signed = True
#                 i += 1
#                 continue
#             elif s[i] >= '0' and s[i] <= '9':
#                 resStr += s[i]
#                 signed = True # 已经遍历到数字则不能再出现正负号
#                 i += 1
#                 continue
#             else:
#                 break

        
#         #print(resStr)
#         res = 0
#         for c in resStr:
#             res = res * 10 + ord(c) - ord('0')
#         if flag:
#             res = -res
        
#         INT_MAX = 2**31
#         if res < - INT_MAX:
#             res = - INT_MAX
#         if res > INT_MAX - 1:
#             res = INT_MAX - 1

#         return res
            
# def main():
#     test = Solution()
#     s = "  -0003472332 with words"
#     res = 0
#     res = test.myAtoi(s)
#     print(res) 

# if __name__ == "__main__":
#     main()

# Python3 自动机  时间复杂度 O(n) 空间复杂度 O(1)       
INT_MAX = 2**31 - 1
INT_MIN = - 2**31

class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        elif c == '+' or c == '-':
            return 1
        elif c.isdigit():
            return 2
        else:
            return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1

class Solution:
    def myAtoi(self, str: str) -> int:
        automaton = Automaton()
        for c in str:
            automaton.get(c)
        return automaton.sign * automaton.ans

# C++ 自动机
# 如果是class定义的类,那么默认的类型就是private
# 如果是struct定义的类，那么默认的类型就是public
class Automaton {
    string state = "start";
    unordered_map<string, vector<string>> table = {
        {"start", {"start", "signed", "in_number", "end"}},
        {"signed", {"end", "end", "in_number", "end"}},
        {"in_number", {"end", "end", "in_number", "end"}},
        {"end", {"end", "end", "end", "end"}}
    };

    int get_col(char c) {
        if (isspace(c)) {
            return 0;
        } else if (c == '+' or c == '-') {
            return 1;
        } else if (isdigit(c)) {
            return 2;
        } else {
            return 3;
        }
    }

public:
    int sign = 1;
    long long ans = 0;

    void get(char c) {
        state = table[state][get_col(c)];
        if (state == "in_number") {
            ans = ans * 10 + c - '0';
            ans = sign==1 ? min(ans, (long long)INT_MAX) : min(ans, -(long long)INT_MIN);
        } else if (state == "signed") {
            sign = c=='+' ? 1 : -1;
        }
    }
};

class Solution {
public:
    int myAtoi(string str) {
        Automaton automaton;
        for (char c : str) {
            automaton.get(c);
        }
        return automaton.sign * automaton.ans;
    }
};

# Java 自动机
class Solution {
    public int myAtoi(String str) {
        Automaton automaton = new Automaton();
        int length = str.length();

        for (int i = 0; i < length; i++) {
            automaton.get(str.charAt(i));
        }

        return (int)(automaton.sign * automaton.ans);
    }
}

class Automaton {
    public int sign = 1;
    public long ans = 0;
    
    private String state = "start";
    private Map<String, String[]> table = new HashMap<String, String[]>() {
        {
            put("start", new String[]{"start", "signed", "in_number", "end"});
            put("signed", new String[]{"end", "end", "in_number", "end"});
            put("in_number", new String[]{"end", "end", "in_number", "end"});
            put("end", new String[]{"end", "end", "end", "end"});
        }
    };

    public void get(char c) {
        state = table.get(state)[get_col(c)];
        if ("in_number".equals(state)) {
            ans = ans * 10 + c - '0';
            ans = sign==1 ? Math.min(ans, (long)Integer.MAX_VALUE) : Math.min(ans, -(long)Integer.MIN_VALUE);
        } else if ("signed".equals(state)) {
            sign = c=='+' ? 1 : -1;
        }
    }

    private int get_col(char c) {
        if (c == ' ') {
            return 0;
        } else if (c == '+' || c == '-') {
            return 1;
        } else if (Character.isDigit(c)) {
            return 2;
        } else {
            return 3;
        }
    }
}