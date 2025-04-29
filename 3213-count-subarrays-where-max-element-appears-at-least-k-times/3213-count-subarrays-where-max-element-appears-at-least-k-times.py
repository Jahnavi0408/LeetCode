class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        count = 0
        l = 0
        freq = 0

        for r in range(len(nums)):
            if nums[r] == max_val:
                freq += 1

            while freq >= k:
                if nums[l] == max_val:
                    freq -= 1
                l += 1
            
            count += l
        
        return count
        