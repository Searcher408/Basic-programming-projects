# Python 3
from typing import Collection, List

# 暴力法 生成所有 2^{2n}个 '(' 和 ')' 字符构成的序列，然后检查每一个是否有效即可
# 时间复杂度：O(2^{2n}n)n)，对于 2^{2n}个序列中的每一个，用于建立和验证该序列的复杂度为 O(n)。
# 空间复杂度：O(n)，除了答案数组之外，所需要的空间取决于递归栈的深度，每一层递归函数需要 O(1)的空间，
# 最多递归 2n 层，因此空间复杂度为 O(n)。
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         def generate(A):
#             if len(A) == 2*n:
#                 if valid(A):
#                     ans.append("".join(A))
#             else:
#                 A.append('(')
#                 generate(A)
#                 A.pop()
#                 A.append(')')
#                 generate(A)
#                 A.pop()

#         def valid(A):
#             bal = 0
#             for c in A:
#                 if c == '(':
#                     bal += 1
#                 else:
#                     bal -= 1
                
#                 if bal < 0:
#                     return False
            
#             return bal == 0
        
#         ans = []
#         generate([])
#         return ans

# 回溯法
# 只在序列仍然保持有效时才添加 '(' or ')'，而不是像 方法一 那样每次添加。
# 可以通过跟踪到目前为止放置的左括号和右括号的数目来做到这一点，
# 如果左括号数量不大于 n，可以放一个左括号。如果右括号数量小于左括号的数量，可以放一个右括号。
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         ans = []

#         def backtrack(S, left, right):
#             if len(S) == 2*n:
#                 ans.append("".join(S))
#                 return
#             if left < n:
#                 S.append('(')
#                 backtrack(S, left+1, right)
#                 S.pop()
#             if right < left:
#                 S.append(')')
#                 backtrack(S, left, right+1)
#                 S.pop()

#         backtrack([], 0, 0)
#         return ans

# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         result = {''} # 初始化为含有一个空字符串的集合，不能初始化为空集，因为需要进入循环 for s in result
        
#         for i in range(n):
#             temp = set() # 初始化为空集
#             for s in result: # 在上一次结果的所有字符串的各个位置插入'()'
#                 for j in range(len(s) + 1):
#                     temp.add(s[:j] + '()' + s[j:])
#             result = temp

#         return list(result)

# def main():
#     test = Solution()
#     n = 3
#     res = test.generateParenthesis(n)
#     print(res)

# if __name__ == "__main__":
#     main()

# Java 暴力法
/**
* 思路:
* (1) 生成所有()可能构成的字符串
* (2) 过滤出其中符合条件的字符串
*
* @param n 数字
* @return 结果
*/

public List<String> generateParenthesis(int n) {
    List<String> all = generateAll(n);
    List<String> resultList = new ArrayList<>();
    for(String string : all) {
        if(isValid(string)) {
            resultList.add(string);
        }
    }
    return resultList;
}

/**
* 生成所有可能的字符串
* @param n 个数
* @param 结果
*/
private List<String> generateAll(final int n) {
    List<String> resultList = new ArrayList<>();
    resultList.add("");
    char[] chars = new char[]{'(', ')'};
    for(int i = 0; i < n*2; i++) {
        List<String> newList = new ArrrayList<>();
        for(String result : resultList) {
            for(char c : chars) {
                newList.add(result+c);
            }
        }
        resultList = newList;
    }
    return resultList;
}

/**
* 是否合法
* @param s 字符串
* @return 结果
*/
private boolean isValid(final String s) {
    int length = s.length();
    int headIx = 0;
    for(int i = 0; i < length; i++) {
        char c = s.charAt(i);
        if('(' == c) {
            headIx++;
        } else {
            if(headIx == 0) {
                return false;
            }
            headIx--;
        }
    }
    return headIx == 0;
}


# 当final修饰变量时，被修饰的变量必须被初始化(赋值)，且后续不能修改其值，实质上是常量；
# 当final修饰方法时，被修饰的方法无法被所在类的子类重写（覆写）；
# 当final修饰类时，被修饰的类不能被继承，并且final类中的所有成员方法都会被隐式地指定为final方法，但成员变量则不会变。
# 详解Java中的final关键字 https://jiang-hao.com/articles/2019/backend-java-final-keyword.html

# Java DFS算法
# 对递归树进行剪枝：
# 第一个有效符号一定是 (
# ( 个数比 ) 少的时候，进行剪枝
# ( 和 ) 的个数都等于 n 的时候，一次遍历就结束了
public List<String> generateParenthesis(int n) {
    List<String> resultList = new ArrayList<>();
    def(resultList, "", 0, 0, n);
    return resultList;
}

/**
* 深度优先遍历
* @param resultList 结果列表
* @param string 字符串
* @param left 左括号
* @param right 右括号
* @param num 位数
*/
private void dfs(List<String> resultList,
                String string,
                int left,
                int right,
                int num) {
    if(left == num && right == num) {
        resultList.add(string);
        return;
    }

    // 左边的括号是可以一直加的
    if(left < num) {
        dfs(resultList, string+"(", left+1, right, num);
    }

    // 对剪枝进行优化，跳过left < right

    // 右括号数量比左括号少时可以添加右括号
    if(right < left) {
        dfs(resultList, string+")", left, right+1, num);
    }
}

# 上面的DFS版本中，String 有过多次的隐式创建，消耗性能
# DFS改良版本，标准的回溯算法，使用StringBuilder替代String, 需要重新设置长度以保证回溯正确

public List<String> generateParenthesis(int n) {
    List<String> resultList = new ArrayList<>();
    StringBuilder stringBuilder = new StringBuilder(n << 1);
    backtrack(resultList, stringBuilder, 0, 0, n);
    return resultList;
}

/**
* 递归处理
* @param resultList 结果列表
* @param stringBuilder 字符串
* @param left 左括号
* @param right 右括号
* @param num 位数
*/
private void backtrack(List<String> resultList,
                        StringBuilder stringBuilder,
                        int left,
                        int right,
                        int num) {
    if(stringBuilder.length() == num << 1) {
        resultList.add(stringBuilder.toString());
        return;
    }

    // 左边的括号是可以一直加的
    if(left < num) {
        backtrack(resultList, stringBuilder.append("("), left+1, right, num);
        // 重新设置
        stringBuilder.setLength(stringBuilder.length()-1);
        // 或者使用 stringBuilder.deleteCharAt(stringBuilder.length()-1);
    }

    if(right < left) {
        backtrack(resultList, stringBuilder.append(")"), left, right+1, num);
        stringBuilder.setLength(stringBuilder.length()-1);
    }
}

# 使用String拼接字符串的时候String每次都新建一个StringBuilder对象，再转为String，
# 相当于递归方法里面每次都新建一个新的String对象，方法外面的String一直没变。
# StringBuilder一直都是一个对象所以要先append，再还原（delete）

# Java BFS, 采用自定义Node节点，然后横向遍历的方式
class Node {
    private String text;
    private int left;
    private int right;

    public Node(String text, int left, int right) {
        this.text = text;
        this.left = left;
        this.right = right;
    }
}

/**
* @param n 数字
* @return 结果
*/
public List<String> generateParenthesis(int n) {
    List<String> res = new ArrayList<>();
    if(n == 0) {
        return res;
    }

    // 从上到下
    Queue<Node> queue = new LinkedList<>();
    Node rootNode = new Node("", 0, 0);
    queue.add(rootNode);
    while (!queue.isEmpty()) {
        Node curNode = queue.remove(); //返回第一个元素，并在队列中删除

        // 最后一层
        if (curNode.left == n && curNode.right == n) {
            res.add(curNode.text);
        }

        if (curNode.left < n) {
            queue.add(new Node(curNode.text + "(", curNode.left + 1, curNode.right));
        }

        if (curNode.right < curNode.left) {
            queue.add(new Node(curNode.text + ")", curNode.left, curNode.right + 1));
        }
    }

    return res;
}

# 队列是一种特殊的线性表，它只允许在表的前端进行删除操作，而在表的后端进行插入操作。
# Java中LinkedList类实现了Queue接口，因此可以把LinkedList当成Queue来用。
# remove() 和 poll() 方法都是从队列中删除第一个元素。
# remove() 的行为与 Collection 接口的版本相似， 但是新的 poll() 方法在用空集合调用时不是抛出异常，只是返回 null。

# Java 动态规划DP
# 核心思路：
# 任何一个括号序列都一定是由 ( 开头，并且第一个 ( 一定有一个唯一与之对应的 )。
# 这样每一个括号序列可以用 (a)b 来表示，其中 a 与 b 分别是一个合法的括号序列（可以为空）。
# 那么要生成所有长度为 2 * n 的括号序列，定义一个函数 generate(n) 来返回所有可能的括号序列。

# 在函数 generate(n) 的过程中：
# 1.需要枚举与第一个 ( 对应的 ) 的位置 2 * i + 1；
# 2.递归调用 generate(i) 即可计算 a 的所有可能性；// a 为括号对数为i的括号组合
# 3.递归调用 generate(n - i - 1) 即可计算 b 的所有可能性； // b 为括号对数为n - i - 1的括号组合，减去1是因为第一对括号已存在
# 4.遍历 a 与 b 的所有可能性并拼接，即可得到所有长度为 2 * n 的括号序列。

# 为了节省计算时间，在每次 generate(i) 函数返回之前，把返回值存储起来，下次再调用 generate(i) 时可以直接返回，不需要再递归计算。

# DP 最核心的两点：
# 1.找到递推公式
# 2.缓存结果，避免重复计算
public List<String> generateParenthesis(int n) {
    // 存放缓存信息
    List<List<String>> cache = new ArrayList<>();

    // 初始化第一个元素列表为[""]
    cache.add(Collection.singletonList(""));
    // singletonList(T) 方法用于返回一个只包含指定对象的不可变列表

    for (int i = 1; i <= n; i++) {
        List<String> cur = new ArrayList<>();
        for (int j = 0; j < i; j++) {
            List<String> str1 = cache.get(j); // 计算 a 的所有可能性
            List<String> str2 = cache.get(i - j - 1); // 计算 b 的所有可能性
            for (String s1 : str1) {
                for (String s2 : str2) {
                    // 枚举右括号的位置
                    cur.add("(" + s1 + ")" + s2);
                }
            }
            cache.add(cur);
        }
        return cache.get(n);
    }
}

# C++ DP
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<vector<string>> v(n+1);
        v[0].push_back("");
        
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                for (string &str1 : v[j]) {
                    for (string & str2 : v[i-j-1]) {
                        v[i].push_back("(" + str1 + ")" + str2);
                    }
                }
            }
        }

        return v[n];
    }
};