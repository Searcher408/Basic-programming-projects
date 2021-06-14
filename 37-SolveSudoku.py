# 题目数据保证输入数独仅有一个解。
# 按照「行优先」的顺序依次枚举每一个空白格中填的数字，通过递归 + 回溯的方法枚举所有可能的填法。
# 当递归到最后一个空白格后，如果仍然没有冲突，说明找到了答案；
# 在递归的过程中，如果当前的空白格不能填下任何一个数字，那么就进行回溯。

# 由于所给出的解题方法均以递归 + 回溯为基础，算法运行的时间（以及时间复杂度）很大程度取决于给定的输入数据，
# 很难找到一个非常精确的渐进紧界。因此这里只给出一个较为宽松的渐进复杂度上界O(9^(9×9))，
# 即最多有 9×9 个空白格，每个格子可以填 [1,9] 中的任意整数。


# Python 递归
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return # 只返回一次，即pos等于空格数的时候
            
            i, j = spaces[pos]
            for digit in range(9):
                if raw[i][digit] == column[j][digit] == block[i // 3][j // 3][digit] == False:
                    board[i][j] = str(digit + 1)
                    raw[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True
                    dfs(pos + 1)
                    raw[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = False
                if valid: # 用于递归结束后每层递归的返回，返回次数即递归深度，即空格数
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
                    raw[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True
        
        dfs(0)


# C++ 递归
class Solution {
private:
    bool raw[9][9]; // 一共9行，标记每行中9个数字出现情况
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
        for (int digit = 0; digit < 9 && !valid; digit++) { // 一旦valid变为true，即达到最大递归深度找到答案，就不再进入循环
            if (!raw[i][digit] && !column[j][digit] && !block[i / 3][j / 3][digit]) {
                board[i][j] = '0' + digit + 1; // 填入了数字之后，要将标记的三个值都置为true
                raw[i][digit] = column[j][digit] = block[i / 3][j / 3][digit] = true;
                dfs(board, pos + 1); // 继续对下一个空白格位置进行递归
                raw[i][digit] = column[j][digit] = block[i / 3][j / 3][digit] = false;
                // 在回溯到当前递归层时，还要将标记的三个值重新置为false。
            }
        }
    }

    void solveSudoku(vector<vector<char>>& board) {
        memset(raw, false, sizeof(raw));
        memset(column, false, sizeof(column));
        memset(block, false, sizeof(block));
        valid = false;

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') { // 空白格
                    spaces.emplace_back(i, j); // emplace_back() 的执行效率比 push_back() 高
                } else {
                    int digit = board[i][j] - '0' - 1;
                    raw[i][digit] = column[j][digit] = block[i / 3][j / 3][digit] = true;
                }
            }
        }

        dfs(board, 0);
    }
};


# 位运算优化
# 方法一中使用了长度为 9 的数组表示每个数字是否出现过。同样也可以借助位运算，仅使用一个整数表示每个数字是否出现过。
# 具体地，数 b 的二进制表示的第 i 位（从低到高，最低位为第 0 位）为 1，当且仅当数字 i+1 已经出现过。
# 例如当 b 的二进制表示为 (011000100)_2时，就表示数字 3，7，8 已经出现过。

# C++
class Solution {
private:
    int raw[9]; // 每个数字表示相应行中9个数字的出现情况
    int column[9]; // 每个数字表示相应列中9个数字的出现情况
    int block[3][3]; // 每个数字表示相应block中9个数字的出现情况
    bool valid;
    vector<pair<int, int>> spaces;

public:
    void flip(int i, int j, int digit) { // flip 快速翻转
        raw[i] ^= (1 << digit); // 与数 1 << i 进行按位异或运算，将第 i 位从 0 变为 1，或从 1 变为 0
        column[j] ^= (1 << digit); 
        block[i / 3][j / 3] ^= (1 << digit);
    }

    void dfs(vector<vector<char>>& board, int pos) {
        if (pos == spaces.size()) {
            valid = true;
            return;
        }

        auto [i, j] = spaces[pos];
        int mask = ~(raw[i] | column[j] | block[i / 3][j / 3]) & 0x1ff; // 0x1ff 低9位为1，高位为0
        // 对于第 i 行第 j 列的位置, (raw[i] | column[j] | block[i / 3][j / 3])中第 k 位为 1，表示该位置不能填入数字 k+1
        // 对这个值进行按位取反运算，那么第 k 位为 1 就表示该位置可以填入数字k+1，就可以通过寻找 1 来进行枚举。
        // 由于在进行按位取反运算后，这个数的高位也全部变成了 1, 
        // 将这个数和 (1 1111 1111)_2 = (1FF)_16进行按位与运算，将所有无关的位设置为0。

        for (; mask && !valid; mask &= (mask - 1)) { 
            int digitMask = mask & (-mask); // 用 b & (−b) 得到 b 二进制表示中最低位的 1，因为(-b)以补码的形式存储，等于∼b+1
            int digit = __builtin_ctz(digitMask); // 通过语言自带的函数得到这个最低位的 1 究竟是第几位（即 i 值）
            flip(i, j, digit);
            board[i][j] = '0' + digit + 1;
            dfs(board, pos + 1);
            flip(i, j, digit);

            // 用 b 和最低位的 1 进行按位异或运算，就可以将其从 b 中去除，这样就可以枚举下一个 1。
            // 同样地也可以用 b 和 b−1 进行按位与运算达到相同的效果: mask &= (mask - 1)
        }
    }

    void solveSudoku(vector<vector<char>>& board) {
        memset(raw, 0, sizeof(raw));
        memset(column, 0, sizeof(column));
        memset(block, 0, sizeof(block));
        valid = false;

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    int digit = board[i][j] - '0' - 1;
                    flip(i, j, digit);
                }
            }
        }

        // 枚举优化，将唯一确定的空白格全部填入对应的数。
        while (true) {
            int modified = false;
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 9; j++) {
                    if (board[i][j] == '.') {
                        int mask = ~(raw[i] | column[j] | block[i / 3][j / 3]) & 0x1ff;
                        if (!(mask & (mask - 1))) {
                            int digit = __builtin_ctz(mask);
                            flip(i, j, digit);
                            board[i][j] = '0' + digit + 1;
                            modified = true;
                        }
                    }
                }
            }
            if (!modified) {
                break; // 跳出循环
            }
        }

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    spaces.emplace_back(i, j);
                }
            }
        }

        dfs(board, 0);
    }
};

# 枚举优化
# 顺着方法二的思路继续优化，如果一个空白格只有唯一的数可以填入，也就是其对应的 b 值和 b-1 进行按位与运算后得到 0
# （即 b 中只有一个二进制位为 1）。此时就可以确定这个空白格填入的数，而不用等到递归时再去处理它。
# 可以首先遍历整个数独，将唯一确定的空白格全部填入对应的数。随后再使用与方法二相同的方法对剩余无法唯一确定的空白格进行递归 + 回溯。

# Python3
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def flip(i: int, j: int, digit: int):
            raw[i] ^= (1 << digit)
            column[j] ^= (1 << digit)
            block[i // 3][j // 3] ^= (1 << digit)

        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return
            
            i, j = spaces[pos]
            mask = ~(raw[i] | column[j] | block[i // 3][j // 3]) & 0x1ff
            while mask:
                digitMask = mask & (-mask) # 得到最低位的 1
                digit = bin(digitMask).count('0') - 1 # 得到这个最低位的 1 究竟是第几位，bin(x)将整数转换为前缀为"0b"的二进制字符串
                board[i][j] = str(digit + 1)
                flip(i, j, digit)
                dfs(pos + 1)
                flip(i, j, digit)
                mask &= (mask - 1)
                if valid:
                    return
            
        raw = [0] * 9
        column = [0] * 9
        block = [[0] * 3 for _ in range(3)]
        valid = False
        spaces = list()

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    digit = int(board[i][j]) - 1
                    flip(i, j, digit)
        
        while True:
            modified = False
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        mask = ~(raw[i] | column[j] | block[i // 3][j // 3]) & 0x1ff
                        if not (mask & (mask - 1)):
                            digit = bin(mask).count("0") - 1
                            flip(i, j, digit)
                            board[i][j] = str(digit + 1)
                            modified = True
            if not modified:
                break
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    spaces.append((i, j))

        dfs(0)
