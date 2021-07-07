# Python3
from collections import defaultdict
from typing import Counter, List

# 哈希表
# orders[i]=[customerNamei,tableNumberi,foodItemi]
# 最终 “结果” 包含两部分：
# title : 由 "Table" + 排序去重的餐品 组成
# 内容 : 由 桌号 + 每件餐品对应的数量 组成
# 基于此，使用 Set 存储 title 相关内容，使用 Map 存储内容相关部分。
# 去重 Map 的部分 Key 为桌号，同时为了快速索引当前桌号「某个餐品的数量」，需要再套一层 Map。
# 即最终存储格式为 桌号 : {餐品 : 个数}。

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        resTable = list()

        # 餐品 (用于构造title)
        foods = set()
        # 桌号 ： {餐品 ： 个数} (用于构造内容)
        orderDict = defaultdict(lambda: defaultdict(int))

        for c, t, f in orders:
            tidx = int(t)
            foods.add(f)
            orderDict[tidx][f] += 1
        # n, m = len(orderDict) + 1, len(foods) + 1

        # 构造 title 并手动排序
        foods = sorted(foods)
        title = list()
        title.append('Table')
        title += foods
        resTable.append(title)

        # 构造内容并手动排序
        for tidx in sorted(orderDict.keys()):
            tableLine = list()
            tableLine.append(str(tidx))
            for food in foods:
                tableLine.append(str(orderDict[tidx][food]))
            resTable.append(tableLine)
        
        return  resTable

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        # 维护两个哈希表，分别存 餐品种类 和 座号-餐品-数量
        food, table = set(), dict()
        for _, t, f in orders:
            food.add(f)
            if t not in table:
                table[t] = Counter() # 创建一个空的Counter
            table[t][f] += 1
        title = ['Table'] + sorted(food)
        n = len(title)
        return [title] + [[k] + [str(table[k][title[i]]) for i in range(1, n)] for k in sorted(table.keys(), key=lambda x: int(x))]

# Python collections.Counter 计数器，计算“可迭代序列中”各个元素（element）的数量。
#对列表作用
# nums = [1,9,9,5,0,8,0,9]  #GNZ48-陈珂生日
# print(Counter(nums))  #Counter({9: 3, 0: 2, 1: 1, 5: 1, 8: 1})
#对字符串作用
# chars = Counter('abcdeabcdabcaba')
# print(temp)  #Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1})
#以上其实是两种使用方法，一种是直接用，一种是实例化以后使用,如果要频繁调用的话，显然后一种更简洁
#查询具体某个元素的个数
# c = Counter('ABBCC')
# print(c['A'])  #1

# C++ 哈希表
class Solution {
public:
    vector<vector<string>> displayTable(vector<vector<string>>& orders) {
        vector<vector<string>> resTable;
        
        set<string> foods;
        unordered_map<int, unordered_map<string, int>> orderDict;
        for (auto & order : orders) {
            string c = order[0], t = order[1], f = order[2];
            int tidx = stoi(t);
            foods.insert(f);
            unordered_map<string, int> m = orderDict[tidx];
            m[f]++;
            orderDict[tidx] = m;
        }

        vector<string> foodsTitle(foods.begin(), foods.end());
        sort(foodsTitle.begin(), foodsTitle.end());
        vector<string> title;
        title.emplace_back("Table");
        for (auto & food : foodsTitle) {
            title.emplace_back(food);
        }
        resTable.emplace_back(title);

        vector<int> orderNums;
        for (auto & [k, v] : orderDict) {
            orderNums.emplace_back(k);
        }
        sort(orderNums.begin(), orderNums.end());
        for (int tidx : orderNums) {
            unordered_map<string, int> m(orderDict[tidx].begin(), orderDict[tidx].end());
            vector<string> tableLine;
            tableLine.emplace_back(to_string(tidx));
            for (auto & food : foodsTitle) {
                tableLine.emplace_back(to_string(m[food]));
            }
            resTable.emplace_back(tableLine);
        }
        return resTable;
    }
};

