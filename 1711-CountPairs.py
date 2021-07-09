# Python3 超时
from collections import defaultdict
from typing import List

class Solution: 
    def countPairs(self, deliciousness: List[int]) -> int:
        res = 0
        # deliciousness.sort()
        n = len(deliciousness)
        for i in range(n - 1):
            for j in range(i + 1, n):
                ans = deliciousness[i] + deliciousness[j]
                count = bin(ans).count('1')
                # count = 0
                # while ans:
                #     count += 1
                #     ans & (ans - 1)
                if count == 1:
                    res += 1
        return res % (10**9 + 7)

# Python3 
class Solution: 
    def countPairs(self, deliciousness: List[int]) -> int:
        res = 0
        # MOD = 10 ** 9 + 7
        maxSum = max(deliciousness) * 2
        mp = defaultdict(int)
        for val in deliciousness:
            tmpSum = 1
            while tmpSum <= maxSum:
                count = mp[tmpSum - val] if (tmpSum - val) in mp else 0
                # res = (res + count) % MOD
                res += count
                tmpSum <<= 1
            mp[val] += 1
        return res % (10**9 + 7)


# C++ 哈希表
# 由于遍历数组时，哈希表中已有的元素的下标一定小于当前元素的下标，
# 因此任意一对元素之和等于 2 的幂的元素都不会被重复计算。
class Solution {
public:
    static constexpr int MOD = 1'000'000'007; // C＋＋11中新增加了用于指示常量表达式的constexpr关键字

    int countPairs(vector<int>& deliciousness) {
        int maxVal = *max_element(deliciousness.begin(), deliciousness.end());
        int maxSum = maxVal * 2;
        int pairs = 0;
        unordered_map<int, int> mp;
        int n = deliciousness.size();
        for (auto& val : deliciousness) {
            for (int sum = 1; sum <= maxSum; sum <<= 1) {
                int count = mp.count(sum - val) ? mp[sum - val] : 0;
                pairs = (pairs + count) % MOD;
            }
            mp[val]++;
        }
        return pairs;
    }
};

# C 哈希表
#include "uthash.h" 

struct HashTable {
    int key, val;
    UT_hash_handle hh; /* makes this structure hashable */
};

const int MOD = 1000000007;

int countPairs(int* deliciousness, int deliciousnessSize) {
    int maxVal = 0;
    for (int i = 0; i < deliciousnessSize; i++) {
        maxVal = fmax(maxVal, deliciousness[i]);
    }
    int maxSum = maxVal * 2;
    int pairs = 0;
    struct HashTable *hashTable = NULL, *tmp;
    
    for (int i = 0; i < deliciousnessSize; i++) {
        int val = deliciousness[i];
        for (int sum = 1; sum <= maxSum; sum <<= 1) {
            int target = sum - val;
            HASH_FIND_INT(hashTable, &target, tmp);
            int count = tmp == NULL ? 0 : tmp->val;
            pairs = (pairs + count) % MOD;
        }
        HASH_FIND_INT(hashTable, &val, tmp); 
        if (tmp == NULL) {
            tmp = malloc(sizeof(struct HashTable));
            tmp->key = val, tmp->val = 1;
            HASH_ADD_INT(hashTable, key, tmp); // HASH_ADD_INT表示添加的键值为int类型
        } else {
            tmp->val++;
        }
    }
    return pairs;
}