# Python3

# 假设n个节点存在二叉排序树的个数是G(n)，1为根节点，2为根节点，...，n为根节点，
# 当1为根节点时，其左子树节点个数为0，右子树节点个数为n-1，
# 同理当2为根节点时，其左子树节点个数为1，右子树节点为n-2，
# 所以可得G(n) = G(0)*G(n-1)+G(1)*(n-2)+...+G(n-1)*G(0)
# G(0) = 1
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]

        return dp[n]
        
