class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count_map = defaultdict(int)
        count_map[0] = 1  
        prefix = 0
        res = 0

        for num in nums:
            if num % modulo == k:
                prefix += 1
            
        
            target = (prefix - k) % modulo
            res += count_map[target]

            
            count_map[prefix % modulo] += 1

        return res