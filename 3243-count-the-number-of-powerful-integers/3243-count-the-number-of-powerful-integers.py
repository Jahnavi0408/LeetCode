class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def fn(val): 
            
            n = len(val) - len(s)
            if n < 0: return 0 
            dp = [[0]*2 for _ in range(n+1)]
            dp[-1][0] = 1
            dp[-1][1] = int(val[n:] >= s)
            for i in range(n-1, -1, -1): 
                dp[i][0] = (1+limit)*dp[i+1][0]
                if int(val[i]) <= limit: dp[i][1] = int(val[i])*dp[i+1][0] + dp[i+1][1]
                else: dp[i][1] = (1+limit)*dp[i+1][0]
            return dp[0][1]
        
        return fn(str(finish)) - fn(str(start-1))

