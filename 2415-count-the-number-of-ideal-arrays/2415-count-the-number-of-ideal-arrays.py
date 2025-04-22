class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7
        max_k = 14  
        
        
        combs = [[0] * (max_k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for k in range(min(i, max_k) + 1):
                combs[i][k] = comb(i, k) % MOD
        
        
        dp = [[0] * (max_k + 1) for _ in range(maxValue + 1)]
        for x in range(1, maxValue + 1):
            dp[x][1] = 1  
        
        
        for k in range(2, max_k + 1):
            for x in range(1, maxValue + 1):
                for m in range(2 * x, maxValue + 1, x):  
                    dp[m][k] = (dp[m][k] + dp[x][k - 1]) % MOD

        
        total = 0
        for x in range(1, maxValue + 1):
            for k in range(1, max_k + 1):
                if dp[x][k] == 0:
                    continue
                total = (total + dp[x][k] * combs[n - 1][k - 1]) % MOD
        
        return total
        