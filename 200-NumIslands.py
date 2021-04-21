# C++ 深度优先搜索 时间复杂度O(MN) 空间复杂度O(MN)
class Solution {
private:
    void dfs(vector<vector<char>>& grid, int r, int c) {
        int nr = grid.size();
        int nc = grid[0].size();

        grid[r][c] = '0';
        if (r-1 >= 0 && grid[r-1][c] == '1') dfs(grid, r-1, c);
        if (r+1 < nr && grid[r+1][c] == '1') dfs(grid, r+1, c);
        if (c-1 >= 0 && grid[r][c-1] == '1') dfs(grid, r, c-1);
        if (c+1 < nc && grid[r][c+1] == '1') dfs(grid, r, c+1);
    }

public:
    int numIslands(vector<vector<char>>& grid) {
        int nr = grid.size();
        if (!nr) return 0;
        int nc = grid[0].size();

        int num_islands = 0;
        for (int r = 0; r < nr; r++) {
            for (int c = 0; c < nc; c++) {
                if (grid[r][c] == '1') {
                    num_islands++;
                    dfs(grid, r, c);
                }
            }
        }

        return num_islands;
    }
};

# C++ 广度优先搜索
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int nr = grid.size();
        if (!nr) return 0;
        int nc = grid[0].size();

        int num_islands = 0;
        for (int r = 0; r < nr; r++) {
            for (int c = 0; c < nc; c++) {
                if (grid[r][c] == '1') {
                    num_islands++;
                    grid[r][c] = '0';
                    queue<pair<int, int>> neighbors;
                    neighbors.push({r, c});

                    while (!neighbors.empty()) {
                        auto rc = neighbors.front();
                        neighbors.pop();
                        int row = rc.first, col = rc.second;
                        if (row-1 >= 0 && grid[row-1][col] == '1') {
                            neighbors.push({row-1, col});
                            grid[row-1][col] = '0';
                        }
                        if (row+1 < nr && grid[row+1][col] == '1') {
                            neighbors.push({row+1, col});
                            grid[row+1][col] = '0';
                        }
                        if (col-1 >= 0 && grid[row][col-1] == '1') {
                            neighbors.push({row, col-1});
                            grid[row][col-1] = '0';                        
                        }
                        if (col+1 < nc && grid[row][col+1] == '1') {
                            neighbors.push({row, col+1});
                            grid[row][col+1] = '0';
                        }
                    }
                }
            }
        }
        return num_islands;
    }
};

# C++ 队列的成员函数
back()返回最后一个元素
empty()如果队列空则返回真
front()返回第一个元素
pop()删除第一个元素
push()在末尾加入一个元素
size()返回队列中元素的个数

头文件：
#include <queue>

声明： 
queue<int> q;

struct point
{
    int x;
    int y;
};
queue<point> que;

一般当一个对象有多个属性的时候，会用结构体struct写多个属性，
而当只有两个属性的时候，就可以使用pair.
pair<int,int> P;        //对象P有两个属性，都是int类型
pair类型有两个属性值，一个first,一个second
int x = P.first;        //访问P的第一个属性值
int y = P.second;       //访问P的第二个属性值