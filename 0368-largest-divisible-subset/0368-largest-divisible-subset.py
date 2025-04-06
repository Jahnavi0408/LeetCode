class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Step 1: Sort the array
        nums.sort()
        n = len(nums)
        

        dp = [1] * n  
        parent = [-1] * n  
        
        
        max_len = 1
        max_index = 0
        
       
        for i in range(1, n):
            for j in range(i):
                
                if nums[i] % nums[j] == 0:
                   
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j
                        
           
            if dp[i] > max_len:
                max_len = dp[i]
                max_index = i
        
        
        result = []
        current = max_index
        while current != -1:
            result.append(nums[current])
            current = parent[current]
        
       
        result.reverse()
        
        return result
        