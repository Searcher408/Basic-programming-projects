# Python3
from typing import List

# 这一类问题都需要先画出树形图，然后编码实现。
# 搜索回溯 不含剪枝优化
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, begin, path, res):
            if target == 0:
                res.append(path)
                return
            
            for i in range(begin, len(candidates)):
                if target - candidates[i] < 0:
                    break
                dfs(candidates, target - candidates[i], i, path + [candidates[i]], res)

        candidates.sort();
        res = list()
        path = list()
        dfs(candidates, target, 0, path, res)
        return res

# Python3 的 [1, 2] + [3] 语法生成了新的列表，一层一层传到根结点以后，直接 res.append(path) 就可以了；
# 基本类型变量在传参的时候是复制，因此变量值的变化在参数里体现就行，所以 Python3 的代码看起来没有「回溯」这个步骤。


# C++ 根据一个数选和不选画树形图
# 时间复杂度：O(S)，其中 S 为所有可行解的长度之和。从分析给出的搜索树可以看出时间复杂度取决于搜索树所有叶子节点的深度之和，
# 即所有可行解的长度之和。在这题中很难给出一个比较紧的上界，O(n×2^n) 是一个比较松的上界。
# 空间复杂度：O(target)。除答案数组外，空间复杂度取决于递归的栈深度，在最差情况下需要递归 O(target) 层。
class Solution {
public:
    void dfs(vector<int>& candidates, int target, vector<vecot<int>>& ans, vector<int>& combine, int idx) {
        if (idx == candidates.size()) {
            return;
        }

        if (target == 0) {
            ans.emplace_back(combine); // 记录所有可行解
            return;
        }

        // 直接跳过candidates中当前idx的数
        dfs(candidates, target, ans, combine, idx + 1);

        // 选择当前idx的数，添加到combine
        if (target - candidates[idx] >= 0) {
            combine.emplace_back(candidates[idx]);
            dfs(candidates, target - candidates[idx], ans, combine, idx); // idx不变，可以重复选取当前idx的数
            combine.pop_back();
        }
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> ans;
        vector<int> combine;
        dfs(candidates, target, ans, combine, 0);
        return ans;
    }
};

# C++ 使用lambda语法糖
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> path;
        int sum = 0, n = candidates.size();

        // std::function<void(int)> f; // 这里表示function的对象f的参数是int，返回值是void
        function<void(int)> dfs = [&] (int begin) {
            if (sum == target) {
                res.emplace_back(begin(path), end(path));
            } else if (sum < target) {
                for (int i = begin; i != n; i++) {
                    path.emplace_back(candidates[i]);
                    sum += candidates[i];
                    dfs(i);
                    sum -= candidates[i];
                    path.pop_back();
                }       
            } else {
                return; // sum > target结束回溯
            }
        };

        dfs(0);
        return res;
    }
};

# Java 对candidates排序，减少回溯次数
# 每一次搜索的时候设置下一轮搜索的起点 begin，从而在搜索的时候对所得解去重
# 备注：如果题目要求，结果集不计算顺序，此时需要按顺序搜索，才能做到不重不漏。
public class Solution {
    private List<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<Integer> path = new ArrayList<>();
        Array.sort(candidates);
        backtrack(path, candidates, target, 0, 0);
        return res;
    }

    private void backtrack(List<Integer> path, int[] candidates, int target, int sum, int begin) {
        if (sum == target) {
            res.add(new ArrayList<>(path));
            return;
        }

        for (int i = begin; i < candidates.length; i++) {
            int rs = candidates[i] + sum;
            if (rs <= target) {
                path.add(candidates[i]);
                backtrack(path, candidates, target, rs, i);
                path.remove(path.size() - 1);
            } else {
                break; // 当rs>target时是直接跳出循环
            }
        }
    }
}

# 完整Java代码，以 target 为 根结点 ，创建一个分支的时做减法，画出树形图
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.List;

public class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {

        List<List<Integer>> res = new ArrayList<>();
        if (len == 0) {
            return res;
        }

        // 排序剪枝
        Arrays.sort(candidates);
        Deque<Integer> path = new ArrayDeque<>();
        dfs(candidates, target, 0, path, res);
        return res;
    }

    private void dfs(int[] candidates, int target, int begin, Deque<Integer> path, List<List<Inter>> res) {
        // 由于进入更深层回溯时，小于0的部分被剪枝，因此递归终止条件值只判断等于0的情况
        if (target == 0) {
            res.add(new ArrayList<>(path));
            return;
        }

        for (int i = begin; i < candidates.length; i++) {
            if (target - candidates[i] < 0) {
                break;
            }

            path.addLast(candidates[i]);
            dfs(candidates, target - candidates, i, path, res);
            path.removeLast();
        }
    }
}