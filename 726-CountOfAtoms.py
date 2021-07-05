# Python3 模拟题 栈 + 哈希表
from collections import defaultdict
from collections import deque


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        map = defaultdict(lambda: 1)
        d = deque([])
        i = idx = 0
        while i < n:
            c = formula[i]
            if c == '(' or c == ')':
                d.append(c)
                i += 1
            else:
                if str.isdigit(c):
                    # 获取完整的数字，并解析出对应的数值
                    j = i
                    while j < n and str.isdigit(formula[j]):
                        j += 1
                    cnt = int(formula[i:j])

                    i = j
                    # 如果栈顶元素是)，说明当前数值可以可以应用给连续一段原子中
                    if d and d[-1] == ')':
                        tmp = []
                        d.pop()
                        while d and d[-1] != '(':
                            cur = d.pop()
                            map[cur] *= cnt
                            tmp.append(cur)
                        d.pop()

                        for k in range(len(tmp) - 1, -1, -1):
                            d.append(tmp[k])
                    
                    # 如果栈顶元素不是)，说明当前数值只能应用给栈顶的原子
                    else:
                        cur = d.pop()
                        map[cur] *= cnt
                        d.append(cur)
                
                else:
                    # 获取完整的原子名
                    j = i + 1
                    while j < n and str.islower(formula[j]):
                        j += 1
                    cur = formula[i:j] + '_' + str(idx)
                    idx += 1            
                    map[cur] = 1

                    i = j
                    d.append(cur)
            
        # 将不同编号的相同原子进行合并
        mm = defaultdict(int)
        for key, cnt in map.items():
            atom = key.split('_')[0]
            mm[atom] += cnt
        
        # 对mm中的key进行排序作为答案
        ans = []
        for key in sorted(mm.keys()):
            if mm[key] > 1:
                ans.append(key + str(mm[key]))
            else:
                ans.append(key)
        return ''.join(ans)

