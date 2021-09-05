# Python3

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1

        a = 0
        b = 1
        c = 1
        res = 0
        while n > 2:
            res = a + b + c
            a = b 
            b = c
            c = res
            n -= 1
        return res

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1

        res = [0]*(n+1)
        res[0] = 0
        res[1] = res[2] = 1
        for i in range(3, n+1):
            res[i] = res[i-1] + res[i-2] + res[i-3]
        return res[n]