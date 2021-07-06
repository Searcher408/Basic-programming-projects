# Python3
from collections import defaultdict
from typing import List

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

# C++ 哈希表
class Solution {
public:
    vector<vector<string>> displayTable(vector<vector<string>>& os) {
        vector<vector<string>> resTable;
        
        set<string> foods;
        unordered_map<int, unordere_map<string, int>>
    }
};