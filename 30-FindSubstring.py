# Python3
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not s or not words:
            return []
        all_len = sum(map(len, words))
        n = len(s)
        words = Counter(words) # 统计“可迭代序列”中每个元素的出现的次数
        res = []
        for i in range(0, n - all_len + 1):
            tmp = s[i:i+all_len]
            flag = True
            for key in words: 
                if words[key] != tmp.count(key):# tmp.count从字符串中间计算，会出现单词截断的问题
                    flag = False
                    break
            if flag:
                res.append(i)
        return res


# 遍历和比较都是线性的，所以时间复杂度：O(n^2)
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not s or not words:
            return []
        one_word = len(words[0])
        all_len = len(words) * one_word
        n = len(s)
        words = Counter(words)
        res = []
        for i in range(0, n - all_len + 1):
            tmp = s[i:i+all_len]
            c_tmp = []
            for j in range(0, all_len, one_word): # 手动切分单词，避免中间截断
                c_tmp.append(tmp[j:j+one_word])
            if Counter(c_tmp) == words:
                res.append(i)
        return res


# 滑动窗口, 在 s 中维护着一个所有单词长度总和的队列, 时间复杂度：O(n)
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not s or not words:
            return []
        one_word = len(words[0])
        word_num = len(words)
        n = len(s)
        words = Counter(words)
        res = []
        for i in range(0, one_word): # 在 s 中的遍历起点选择为n mod one_word, 即[0, one_word)
            cur_cnt = 0
            left = i
            right = i
            cur_Counter = Counter()
            while right + one_word <= n:
                w = s[right:right + one_word]
                right += one_word
                cur_Counter[w] += 1
                cur_cnt += 1
                while cur_Counter[w] > words[w]:
                    left_w = s[left:left + one_word]
                    left += one_word
                    cur_Counter[left_w] -= 1
                    cur_cnt -= 1
                if cur_cnt == word_num:
                    res.append(left)
        return res

# 优化
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not s or not words:
            return []
        one_word = len(words[0])
        word_num = len(words)
        n = len(s)
        if n < one_word * word_num:
            return []
        words = Counter(words)
        res = []
        for i in range(0, one_word):
            cur_cnt = 0
            left = i
            right = i
            cur_Counter = Counter()
            while right + one_word <= n:
                w = s[right:right + one_word]
                right += one_word
                if w not in words: # 子串要与 words 中的单词完全匹配，中间不能有其他字符
                    left = right
                    cur_Counter.clear()
                    cur_cnt = 0
                else:
                    cur_Counter[w] += 1
                    cur_cnt += 1
                    while cur_Counter[w] > words[w]:
                        left_w = s[left:left+one_word]
                        left += one_word
                        cur_Counter[left_w] -= 1
                        cur_cnt -= 1
                    if cur_cnt == word_num:
                        res.append(left)
        return res

# C++ 多起点滑动窗口
class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
         if (s.empty() || words.empty()) {
            return {};
        }
        vector<int> res;
        int n = s.size(), m = words.size(), d = words[0].size();
        int len = d * m;
        if (n < len) {
            return {};
        }
        unordered_map<string, int> um;
        for (string w : words) {
            um[w]++;
        }

        vector<unordered_map<string, int>> vum(d); // 多起点初始化map，n%d = [0, d)
        for (int i = 0; i < d && i + len <= n; i++) {
            for (int j = i; j < i + len; j += d) {
                string t = s.substr(j, d);
                vum[i][t]++;
            }
            if (vum[i] == um) {
                res.emplace_back(i);
            }
        }

        // 滑动窗口
        for (int i = d; i + len <= n; i++) {
            int r = i % d;
            string ta = s.substr(i - d, d), tb = s.substr(i + len - d, d);
            if(--vum[r][ta] == 0) {
                vum[r].erase(ta);
            }
            vum[r][tb]++;
            if (vum[r] == um) {
                res.emplace_back(i);
            }
        }

        return res;
    }
};

# C++ 暴力
class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        if (s.empty() || words.empty()) {
            return {}; // return vector<int>();
        }
        int n = words.size(), m = words[0].size(), j = 0;
        if (s.size() < m * n) {
            return {};
        }
        vector<int> res;
        unordered_map<string, int> um, tmp_um;
        for (auto word : words) {
            um[word]++;
        }
        string str = "";
        for (int i = 0; i + m * n <= s.size(); i++) {
            for (j = i; j < i + m * n; j += m) {
                str = s.substr(j, m);
                if (um.find(str) == um.end()) {
                    break; // 子串要与 words 中的单词完全匹配，中间不能有其他字符
                }
                tmp_um[str]++;
            }
            if (j == i + m * n && tmp_um == um) {
                res.push_back(i);
            }
            tmp_um.clear();
        }
        return res;
    }
};

# C++ 优化
class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        if (s.empty() || words.empty()) {
            return {};
        }
        
        int n = s.size(), m = words.size(), d = words[0].size();
        int len = d * m;
        if (n < len) {
            return {};
        }

        vector<int> res;
        unordered_map<string, int> um, tmp_um; 
        for (auto w : words) {
            um[w]++;
        }

        for (int i = 0; i < d; i++) {
            int cnt = 0;
            int left = i;
            int right = i;
            tmp_um.clear();
            
            while (right + d <= n) {
                string right_w = s.substr(right, d);
                right += d;
                if (um.find(right_w) == um.end()) {  // 子串要与 words 中的单词完全匹配，中间不能有其他字符
                    left = right;
                    tmp_um.clear();
                    cnt = 0;
                } else {
                    tmp_um[right_w]++;
                    cnt++;
                    while (tmp_um[right_w] > um[right_w]) {
                        string left_w = s.substr(left, d);
                        left += d;
                        tmp_um[left_w]--;
                        cnt--;
                    }
                    if (cnt == m) {
                        res.push_back(left);
                    }
                }
            }
        }
        return res;
    }
};