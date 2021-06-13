# Python
from typing import List

# 递归
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return
            
            i, j = spaces[pos]
            for digit in range(9):
                if raw[i][digit] == column[j][digit] == block[i // 3][j // 3][digit] == False:
                    board[i][j] = str(digit + 1)
                    raw[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True
                    dfs(pos + 1)
                    raw[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = False
                if valid:
                    return
        
        raw = [[False] * 9 for _ in range(9)]
        column = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _c in range(3)] for _r in range(3)]
        valid = False
        spaces = list()

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    raw[i][digit] = column[j][digit] = block[i // 3][j // 3] = True
        
        dfs(0)

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return
            
            i, j = spaces[pos]
            for digit in range(9):
                if raw[i][digit] == column[j][digit] == block[i // 3][j // 3][digit] == False:
                    board[i][j] = str(digit + 1)
                    raw[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True
                    dfs(pos + 1)
                    raw[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = False
                if valid:
                    return
            
        raw = [[False] * 9 for _ in range(9)]
        column = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _c in range(3)] for _r in range(3)]
        valid = False
        spaces = list()

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    raw[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True

        dfs(0)


# 按照「行优先」的顺序依次枚举每一个空白格中填的数字，通过递归 + 回溯的方法枚举所有可能的填法。
# 当递归到最后一个空白格后，如果仍然没有冲突，说明找到了答案；
# 在递归的过程中，如果当前的空白格不能填下任何一个数字，那么就进行回溯。

# 由于所给出的解题方法均以递归 + 回溯为基础，算法运行的时间（以及时间复杂度）很大程度取决于给定的输入数据，
# 很难找到一个非常精确的渐进紧界。因此这里只给出一个较为宽松的渐进复杂度上界O(9^(9×9))，
# 即最多有 9×9 个空白格，每个格子可以填 [1,9] 中的任意整数。

# C++ 递归
class Solution {
private:
    bool line[9][9]; // 一共9行，标记每行中9个数字出现情况
    bool column[9][9]; // 一共9列，标记每列中9个数字出现情况
    bool block[3][3][9]; // 一共3*3个区块，标记每个block中9个数字出现情况
    bool valid; // 标记是否还有空白格进行递归
    vector<pair<int, int>> spaces; // 存储空白格的位置

public:
    void dfs(vector<vector<char>>& board, int pos) {
        if (pos == spaces.size()) { // pos记录递归的空白格数，达到spaces存储数量说明递归结束
            valid = true;
            return;
        }

        auto [i, j] = spaces[pos];
        for (int digit = 0; digit < 9 && !valid; digit++) {
            if (!line[i][digit] && !column[j][digit] && !block[i / 3][j / 3][digit]) {
                board[i][j] = '0' + digit + 1; // 填入了数字之后，要将标记的三个值都置为true
                line[i][digit] = column[j][digit] = block[i / 3][j / 3][digit] = true;
                dfs(board, pos + 1); // 继续对下一个空白格位置进行递归
                line[i][digit] = column[j][digit] = block[i / 3][j / 3][digit] = false;
                // 在回溯到当前递归层时，还要将标记的三个值重新置为false。
            }
        }
    }

    void solveSudoku(vector<vector<char>>& board) {
        memset(line, false, sizeof(line));
        memset(column, false, sizeof(column));
        memset(block, false, sizeof(block));
        valid = false;

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') { // 空白格
                    spaces.emplace_back(i, j); // emplace_back() 的执行效率比 push_back() 高
                } else {
                    int digit = board[i][j] - '0' - 1;
                    line[i][digit] = column[j][digit] = block[i / 3][j / 3][digit] = true;
                }
            }
        }

        dfs(board, 0);
    }
};