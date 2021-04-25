# Python3
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        n = min(numRows, len(s))

        rows = [""]*n
        curRow = 0
        goingDown = False

        for c in s:
            rows[curRow] += c
            #print(rows)
            if curRow == 0 or curRow == n-1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1

        res = ""
        for i in range(n):
            res += rows[i]

        return res

def main():
    test = Solution()
    res = test.convert("ABC" , 2)
    print(res)

if __name__ == "__main__":
    main()


# # C++ 按行排序 时间复杂度 O(n) 空间复杂度 O(n) 
# class Solution {
# public:
#     string convert(string s, int numRows) {
#         if (numRows == 1) return s;

#         vector<string> rows(min(numRows, int(s.size()))); # 使用列表表示Z字形图案中的非空行
#         int curRow = 0;
#         bool goingDown = false;

#         for (char c : s) {
#             rows[curRow] += c;
#             if (curRow == 0 || curRow == numRows - 1) {
#                 goingDown = !goingDown;
#                 curRow += goingDown ? 1 : -1;
#             }
#         }

#         string ret;
#         for (string row : rows) {
#             ret += row;
#         }
#         return ret;
#     }
# };

# # Java 按行排序
# class Solution {
#     public String convert(String s, int numRows) {
#         if (numRows == 1) {
#             return s;
#         }

#         List<StringBuilder> rows = new ArrayList<>();
#         for (int i = 0; i < Math.min(numRows, s.length()); i++) {
#             rows.add(new StringBuilder());
#         }

#         int curRow = 0;
#         boolean goingDown = false;

#         for (char c : s.toCharArray()) {
#             rows.get(curRow).append(c);
#             if (curRow == 0 || curRow == numRows - 1) {
#                 goingDown = !goingDown;
#             }
#             curRow += goingDown ? 1 : -1;
#         }

#         StringBuilder ret = new StringBuilder();
#         for (StringBuilder row : rows) {
#             ret.append(row);
#         }

#         return ret.toString();
#     }
# }

# C++ 按行访问 时间复杂度 O(n) 
class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) {
            return s;
        }

        string ret;
        int n = s.size();
        int cycleLen = 2 * numRows - 2; # 周期规律

        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j + i < n; j += cycleLen) {
                ret += s[j + i];
                if (i != 0 && i != numRows - 1 && j + cycleLen - i < n) {
                    ret += s[j + cycleLen - i];
                }
            }
        }

        return ret;
    }
};

# Java
class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1) {
            return s;
        }

        StringBuilder ret = new StringBuilder();
        int n = s.length();
        int cycleLen = 2 * numRows - 2;

        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j + i < n; j += cycleLen) {
                ret.append(s.charAt(j + i));
                if (i != 0 && i != numRows - 1 && j + cycleLen - i < n) {
                    ret.append(s.charAt(j + cycleLen - i));
                }
            }
        }

        return ret.toString();
    }
}