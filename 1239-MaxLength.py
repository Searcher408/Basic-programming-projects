# Python3
from typing import List


# 回溯 + 位运算
# 需要计算可行解的长度，可行解具体是什么以及各个字符的顺序不用考虑。因此构成可行解的每个字符串均可以视作一个字符集合，且集合不含重复元素。
# 用一个二进制数来表示该字符串的字符集合，第 i 位为 1 表示集合中含有第 i 个小写字母，为 0 表示集合中不含有第 i 个小写字母。
# 时间复杂度：O(∣Σ∣+2^n)。其中∣Σ∣ 是 arr 中所有字符串的长度之和，n 是 arr 的长度。
# 遍历所有字符串需要O(∣Σ∣)，回溯时由于每个元素有选或不选两种情况，最坏情况下会有 2^n种组合方式。 
# 空间复杂度：O(n)。
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = list()
        for s in arr:
            mask = 0
            for c in s:
                idx = ord(c) - ord('a')
                if ((mask >> idx) & 1): # 若mask已有c,则s含有重复字母，无法构成可行解
                    mask = 0
                    break
                mask |= 1 << idx # 将c加入mask中标记
            if mask > 0:
                masks.append(mask) # 将所有的有效字符串加入标记
        ans = 0

        # pos 表示当前递归到了数组masks中的第pos个数，mask表示当前连接得到的字符串对应二进制数为mask
        def backtrack(pos: int, mask: int) -> None:
            if pos == len(masks):
                nonlocal ans
                ans = max(ans, bin(mask).count('1'))
                return

            if (mask & masks[pos]) == 0: # mask 和 mask[pos] 无公共元素
                backtrack(pos + 1, mask | masks[pos])
            backtrack(pos + 1, mask)

        backtrack(0, 0)
        return ans
       

if __name__ == "__main__":
    test = Solution()
    arr = ["un","iq","ue"] 
    res = test.maxLength(arr)
    print(res)

# C++
class Solution {
public:
    int maxLength(vector<string> &arr) {
        vector<int> masks;
        for (string &s : arr) {
            int mask = 0;
            for (char c : s) {
                c -= 'a';
                if ((mask >> c) & 1) {
                    mask = 0;
                    break;
                }
                mask |= 1 << c;
            }
            if (mask > 0) {
                masks.push_back(mask);
            }
        }

        int ans = 0;
        function<void(int, int)> backtrack = [&](int pos, int mask) {
            if (pos == masks.size()) {
                ans = max(ans, __builtin_popcount(mask));
                return;
            }
            if ((mask & masks[pos]) == 0) {
                backtrack(pos + 1, mask | masks[pos]);
            }
            backtrack(pos + 1, mask);
        };

        backtrack(0, 0);
        return ans;
    }
};

# 迭代 + 位运算
# 遍历arr，维护前 i 个字符串构成的可行解集合，记作masks。初始时，可行解集合仅包含一个空字符串。
# 若 arr[i+1] 中无重复字符，则将其与masks 中的字符串连接，若连接后仍无重复字符，则将连接后的新字符串加入到 masks 中，
# 这样就得到了前i+1个字符串构成的可行解集合。遍历结束后，masks 即为 arr 构成的所有可行解，求出其中最长的可行解即为答案。
# 时间复杂度：O(∣Σ∣+2^n)。其中∣Σ∣ 是 arr 中所有字符串的长度之和，n 是 arr 的长度。
# 遍历所有字符串需要O(∣Σ∣)，每次循环会将 masks 的大小增加至多一倍。 
# 空间复杂度：O(2^n)。由于最坏情况下arr 的所有子集都能构成可行解，这有 2^n个，这种情况下遍历结束后的masks 的长度为 2^n。
# Python3
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0
        masks = [0]
        for s in arr:
            mask = 0
            for c in s:
                idx = ord(c) - ord('a')
                if ((mask >> idx) & 1):
                    mask = 0
                    break
            if mask == 0:
                continue

            n = len(masks)
            for i in range(n):
                m = masks[i]
                if (m & mask) == 0: # m 和 mask 无公共元素
                    masks.append(m | mask)
                    ans = max(ans, bin(m | mask).count('1'))
        
        return ans


# Java
class Solution {
    public int maxLength(List<String> arr) {
        int ans = 0;
        List<Integer> masks = new ArrayList<Integer>();

        masks.add(0);
        for (String s : arr) {
            int mask = 0;
            for (int i = 0; i < s.length(); i++) {
                int c = s.charAt(i) - 'a';
                if (((mask >> c) & 1) ! = 0) {
                    mask = 0;
                    break;
                }
                mask |= 1 << c;
            }
            if (mask == 0) {
                continue
            }

            int n = masks.size();
            for (int i = 0; i < n; i++) {
                int m = masks.get(i);
                if ((m & mask) == 0) {
                    masks.add(m | mask);
                    ans = Math.max(ans, Integer.bitCount(m | mask));
                }
            }
        }
        
        return ans;
    }
}

