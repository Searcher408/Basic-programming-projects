# Python3
from _typeshed import OpenBinaryMode
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """


# X X X X
# X O O X
# X X O X
# X O O X
# 这道题拿到基本就可以确定是图的DFS、BFS遍历的题目
# 题目中说被包围的区间不会存在于边界上，所以边界上的 O 要特殊处理。
# 将与边界连通的O替换为#作为占位符，待搜索结束后，遇到O就替换为X，遇到#替换为O
# 问题转化为，如何寻找和边界连通的 O？从边界出发，对图进行DFS和BFS即可
# DFS 递归。最常用，如二叉树的先序遍历。
# DFS 非递归。一般用 stack。
# BFS 递归。如二叉树中递归进行层序遍历。
# BFS 非递归。一般用队列存储。

# DFS 递归
# Java
class Solution {
    public void solve(char[][] board) {
        if (board == null) return;
        int m = board.length;
        int n = board[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                boolean isEdge = i == 0 || j == 0 || i == m-1 || j == n-1;
                if (isEdge && board[i][j] == 'O') {
                    DFS(board, i, j); // 从边界上的O开始搜索
                }
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                }
                if (board[i][j] == '#') {
                    board[i][j] = 'O';
                }
            }
        }
    }

    public void DFS(char[][] board, int i, int j) {
        if (i < 0 || j < 0 || i >= board.length || j >= board[0].length || board[i][j] == 'X' || board[i][j] == '#') {
            // board[i][j] == '#' 说明已经搜索过了
            return;
        }
        board[i][j] = '#';
        DFS(board, i - 1, j); // 上
        DFS(board, i + 1, j); // 下
        DFS(board, i, j - 1); // 左
        DFS(board, i, j + 1); // 右
    }
}

# DFS 非递归，使用stack记录每一次遍历过的位置，具有先进后出的特点。
# 定义一个内部类Pos来标记横坐标和纵坐标。在非递归过程中，每次查看栈顶，但并不出栈，直到这个位置上下左右都搜索不到时才出栈。
# Java
class Solution {
    public class Pos {
        int i;
        int j;
        Pos(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }

    public void solve(char[][] board) {
        if (board == null) return;
        int m = board.length;
        int n = board[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // 从边界第一个O开始搜索
                boolean isEdge = i == 0 || j == 0 || i == m-1 || j == n-1;
                if (isEdge && board[i][j] == 'O') {
                    DFS(board, i, j);
                }
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                }
                if (board[i][j] == '#') {
                    board[i][j] = 'O';
                }
            }
        }
    }

    public void DFS(char[][] board, int i, int j) {
        Stack<Pos> stack = new Stack<>();
        stack.push(new Pos(i, j));
        board[i][j] = '#';
        while (!stack.isEmpty()) {
            // 取出当前栈顶，但不出栈
            Pos cur = stack.peek();

            // 上
            if (cur.i - 1 >= 0 && board[cur.i - 1][cur.j] == 'O') {
                stack.push(new Pos(cur.i - 1, cur.j));
                board[cur.i - 1][cur.j] = '#';
                continue;
            }

            // 下
            if (cur.i + 1 <= board.length - 1 && board[cur.i + 1][cur.j] == 'O') {
                stack.push(new Pos(cur.i + 1, cur.j));
                board[cur.i + 1][cur.j] = '#';
                continue;
            }

            // 左
            if (cur.j - 1 >= 0 && board[cur.i][cur.j - 1] == 'O') {
                stack.push(new Pos(cur.i, cur.j - 1));
                board[cur.i][cur.j - 1] = '#';
                continue;
            }

            // 右
            if (cur.j + 1 <= board[0].length - 1 && board[cur.i][cur.j + 1] == 'O') {
                stack.push(new Pos(cur.i, cur.j + 1));
                board[cur.i][cur.j + 1] = '#';
                continue;
            }

            // 如果上下左右都搜索不到，则本次搜索结束，出栈
            stack.pop();
        }
    }
}

# BFS 非递归，使用队列记录状态，先进先出。
# 在DFS中搜索上下左右，只要搜索到一个满足条件就顺着该方向继续搜索，所以DFS代码中只要满足条件就入栈，
# 然后continue本次搜索，进行下一次搜索，直到搜索到没有满足条件的时候出栈。
# BFS中要把上下左右满足条件的都入队，搜索的时候不能continue。
# Java
class Solution {
    public class Pos {
        int i;
        int j;
        Pos(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }

    public void solve(char[][] board) {
        if (board == null) return;
        int m = board.length;
        int n = board[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // 从边缘第一个O开始搜索
                boolean isEdge = i == 0 || j == 0 || i == m-1 || j == n-1;
                if (isEdge && board[i][j] == 'O') {
                    BFS(board, i, j);
                }
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                }
                if (board[i][j] == '#') {
                    board[i][j] = 'O';
                }
            }
        }
    }

    public void BFS(char[][] board, int i, int j) {
        Queue<Pos> queue = new LinkedList<>();
        queue.add(new Pos(i, j));
        board[i][j] = '#';
        while (!queue.isEmpty()) {
            Pos cur = queue.poll();

            // 上
            if (cur.i - 1 >= 0 && board[cur.i - 1][cur.j] == 'O') {
                queue.add(new Pos(cur.i - 1, cur.j));
                board[cur.i - 1, cur.j] = '#';
                // 没有continue
            }

            // 下
            if (cur.i + 1 <= board.length - 1 && board[cur.i + 1][cur.j] == 'O') {
                queue.add(new Pos(cur.i + 1, cur.j));
                board[cur.i + 1][cur.j] = '#';
            }

            // 左
            if (cur.j - 1 >= 0 && board[cur.i][cur.j - 1] == 'O') {
                queue.add(new Pos(cur.i, cur.j - 1));
                board[cur.i][cur.j - 1] = '#';
            }

            // 右
            if (cur.j + 1 <= board[0].length - 1 && board[cur.i][cur.j + 1] == 'O') {
                queue.add(new Pos(cur.i, cur.j + 1));
                board[cur.i][cur.j + 1] = '#';
            }
        }
    }
}

# 并查集常用来解决连通性问题，即将一个图中连通的部分划分出来。当判断图中两个点之间是否存在路径时，可以判断它们是否在一个连通区域。 
# 这道题其实求解的就是和边界的 O 在一个连通区域的的问题。

# 并查集的思想就是，同一个连通区域内的所有点的根节点是同一个。将每个点映射成一个数字。先假设每个点的根节点就是它们自己，
# 然后以此输入连通的点对，然后将其中一个点的根节点赋成另一个节点的根节点，这样这两个点所在连通区域又相互连通了。
# 并查集的主要操作有：
# find(int m)：这是并查集的基本操作，查找 m 的根节点。
# isConnected(int m, int n)：判断 m，n 两个点是否在一个连通区域。
# union(int m, int n):合并 m，n 两个点所在的连通区域。
class UnionFind {
    int[] parents;

    public UnionFind(int totalNodes) {
        parents = new int[totalNodes];
        for (int i = 0; i < totalNodes; i++) {
            parents[i] = i;
        }
    }

    // 合并连通区域是通过find来操作的，即看这两个节点是否在一个连通区域内。
    void union(int node1, int node2) {
        int root1 = find(node1);
        int root2 = find(node2);
        if (root1 != root2) {
            parents[root2] = root1;
        }
    }

    int find(int node) {
        while (parents[node] != node) {
            // 当前节点的父节点指向父节点的父节点。
            // 保证一个连通区域最终的parents只有一个。
            parents[node] = parents[parents[node]];
            node = parents[node];
        }
        return node;
    }

    boolean isConnected(int node1, int node2) {
        return find(node1) == find(node2);
    }
}

# 把所有边界上的 O 看做一个连通区域。遇到 O 就执行并查集合并操作，这样所有的 O 就会被分成两类：
# 和边界上的 O 在一个连通区域内的。这些 O 我们保留。
# 不和边界上的 O 在一个连通区域内的。这些 O 就是被包围的，替换。
# 由于并查集一般用一维数组来记录，方便查找 parants，所以将二维坐标用 node 函数转化为一维坐标。

# 并查集实现参考算法第四版1.5节，UFS效率不高从单点'O'的重复访问次数上就能看出来，
# 每个O和相邻O合并时O会被访问多次，但BFS不存在该问题，所以效率高很多
class Solution {

    //并查集类
    class UnionFind{
        private int[] ID;
        private int[] treeSize;
        public UnionFind(int N){
            ID = new int[N];
            treeSize = new int[N];
            for(int i = 0; i < N; i++){
                ID[i] = i;
                treeSize[i] = 1;
            }
        }

        public int find(int i){
            //查找当前树的根节点
            int root = i;
            while(root != ID[root])
                root = ID[root];

            //路径压缩
            int next;
            while(i != ID[i]){
                next = ID[i];
                ID[i] = root;
                i = next;
            }
            return root;
        }

        public boolean connected(int p, int q){
            return find(p) == find(q);
        }

        public void union(int p, int q){
            if(find(p) == find(q))
                return;
            if(treeSize[p] < treeSize[q]) //小树链接到大树上
                ID[ID[p]] = ID[q]; //在调用find后，　路径被压缩，　因此ID[p]即为根节点, 同理ID[q]也为根节点
            else
                ID[ID[q]] = ID[p];
        }    
    }

    //将二维坐标转化为一维坐标, 便于并查集使用
    //ｘ为二维数组的一维索引，　ｙ为二维数组的二维索引
    private int flatternTowDim(int x, int y, int width){
        return x * width + y;
    }

    public void solve(char[][] board) {
        if(board.length == 0) return;
        int len = board.length;
        int width = board[0].length;
        int boardSize = len * width;
        UnionFind uf = new UnionFind(boardSize+1);
        //添加一个虚拟节点，所有位于边界的Ｏ节点均与该虚拟节点相连接
        int i, j;
        for(i = 0; i < board.length; i++){
            for(j = 0; j < board[0].length; j++){
                if((i == 0 || i == board.length-1 || j == 0 || j == board[0].length-1) && board[i][j]=='O')
                    uf.union(flatternTowDim(i, j, width), boardSize);
            }
        }

        //遍历搜索相邻的Ｏ，添加到并查集中
        for(i = 0; i < board.length; i++){
            for(j = 0;j < board[0].length; j++){
                if(board[i][j] == 'O'){
                    //将当前Ｏ点与其上下左右四个方向的Ｏ点相连接
                    if(i-1 >=0 && board[i-1][j] == 'O')
                        uf.union(flatternTowDim(i-1, j, width), flatternTowDim(i, j, width));
                    if(i+1 < board.length && board[i+1][j] == 'O')
                        uf.union(flatternTowDim(i+1, j, width), flatternTowDim(i, j, width));
                    if(j-1 >= 0 && board[i][j-1] == 'O')
                        uf.union(flatternTowDim(i, j-1, width), flatternTowDim(i, j, width));
                    if(j+1 <= board[0].length && board[i][j] == 'O')
                        uf.union(flatternTowDim(i, j+1, width), flatternTowDim(i, j, width));
                }
            }
        }

        //将所有与边界节点不相连的＇Ｏ＇点替换为＇Ｘ＇
        for(i = 0; i < board.length; i++){
            for(j = 0; j < board[0].length; j++){
                if(board[i][j] == 'O' && !uf.connected(flatternTowDim(i, j, width), boardSize))
                    board[i][j] = 'X';
            }
        }
    }
}