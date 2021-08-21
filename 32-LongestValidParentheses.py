# Python3
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0  
        stk = list()
        mark = [0]*len(s)
        for i in range(len(s)):
            if s[i] == '(':
                stk.append(i)
            elif s[i] == ')':
                if not stk:
                    mark[i] = 1
                else:
                    stk.pop()
        while stk:
            mark[stk[-1]] = 1
            stk.pop()
        
        cnt = 0
        for j in range(len(s)):
            if mark[j] == 1:
                cnt = 0
            else:
                cnt += 1
                res = max(cnt, res)

        return res
        
# C++
class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> stk;
        vector<bool> mark(s.length());
        for (int i = 0; i < mark.size(); i++) {
            mark[i] = 0;
        }
        int left = 0, len = 0, ans = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(') {
                stk.push(i);
            } else {
                if (stk.empty()) { // 标记多余的右括号
                    mark[i] = 1;
                } else {
                    stk.pop();
                }
            }
        }

        while (!stk.empty()) { // 标记多余的左括号
            mark[stk.top()] = 1;
            stk.pop();
        }

        // 寻找最长的连续的0（标记）的长度
        for (int i = 0; i < s.length(); i++) {
            if (mark[i]) {
                len = 0;
                continue;
            }
            len++;
            ans = max(ans, len);
        }
        return ans;
    }
};