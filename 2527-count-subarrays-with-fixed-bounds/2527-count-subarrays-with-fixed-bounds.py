class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        last_minK = last_maxK = last_invalid = -1
        ans = 0

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                last_invalid = i
            if num == minK:
                last_minK = i
            if num == maxK:
                last_maxK = i
            ans += max(0, min(last_minK, last_maxK) - last_invalid)
        
        return ans
        