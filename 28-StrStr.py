# Python3 超时
class Solution: 
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: # 当 needle 是空字符串时返回 0 
            return 0
        n = len(haystack)
        m = len(needle)
        for i in range(n):
            if haystack[i] == needle[0] and i + m <= n:
                j = 0
                while j < m and haystack[i + j] == needle[j]:
                    j += 1
                if j == m:
                    return i
        return - 1

class Solution: 
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: # 当 needle 是空字符串时返回 0 
            return 0
        n = len(haystack)
        m = len(needle)
        for i in range(n):
            if haystack[i] == needle[0] and i + m <= n:
                if haystack[i:i+m] == needle:
                    return i
        return - 1

# 本题是经典的字符串单模匹配的模型，因此可以使用字符串匹配算法解决，
# 常见的字符串匹配算法包括暴力匹配、Knuth-Morris-Pratt 算法、Boyer-Moore 算法、Sunday 算法等。

# C 暴力匹配
# 让字符串 needle 与字符串 haystack 的所有长度为 m 的子串均匹配一次
int strStr(char* haystack, char* needle) {
    int n = strlen(haystack), m = strlen(needle);
    for (int i = 0; i + m <= n; i++) {
        bool flag = true;
        for (int j = 0; j < m; j++) {
            if (haystack[i + j] != needle[j]) {
                flag = false;
                break;
            }
        }
        if (flag) {
            return i;
        }
    }
    return -1;
}

# C KMP算法
# 时间复杂度：O(n+m)，其中 n 是字符串haystack 的长度，m 是字符串needle 的长度。至多需要遍历两字符串一次。
# 空间复杂度：O(m)，其中 m 是字符串needle 的长度。只需要保存字符串needle 的前缀。
# KMP算法（全称Knuth-Morris-Pratt字符串查找算法，由三位发明者的姓氏命名）可以在文本串s中快速查找模式串p。
# 核心为前缀函数，对于长度为 m 的字符串 s，其前缀函数 π(i)(0≤i<m) 
# 表示 s 的子串 s[0:i] 的最长的相等的真前缀与真后缀的长度。真前缀与真后缀的定义为不等于自身的的前缀与后缀。
# 如果不存在符合条件的前后缀则 π(i)=0。有了前缀函数就可以快速地计算出模式串在主串中的每一次出现。
# 长度为 m 的字符串 s 的所有前缀函数的求解算法的总时间复杂度是严格 O(m) 的，且该求解算法是增量算法，
# 即可以一边读入字符串，一边求解当前读入位的前缀函数。
























void kmp_init(const char *s, int *prefix, size_t size) {
    prefix[0] = 0;
    for (size_t i = 1; i < size; i++) {
        if (s[i] == s[prefix[i - 1]]) {
            prefix[i] = prefix[i - 1] + 1;
        } else {
            int j = i - 1;
            while (prefix[j] > 0 && s[prefix[j]] != s[i]) {
                j = prefix[j] - 1;
            }
            if (prefix[j] > 0) {
                prefix[i] = prefix[j] + 1;
            } else {
                prefix[i] = (s[i] == s[0]);
            }
        }
    }
}

int strStr(const char *src, const char *dest) {
    if (!dest || !src) {
        return -1;
    }
    if (!*dest) {
        return 0;
    }
    size_t size = strlen(dest);
    int *prefix = malloc(sizeof(int) * size);
    kmp_init(dest, prefix, size);
    size_t i, j;
    for (i = j = 0; src[i] && j < size; i++) {
        if (dest[j] == src[i]) {
            j++;
        } else if (j) {
            while (prefix[j - 1] > 0 && dest[prefix[j - 1]] != src[i]) {
                j = prefix[j - 1];
            }
            if (prefix[j - 1] > 0) {
                j = prefix[j - 1] + 1;
            } else {
                j = (dest[0] == src[i]);
            }
        }
    }
    free(prefix);
    if (j < size) {
        return -1;
    }
    return i - size;
}