class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        for k in range((n // 3) + 1):
            remaining = nums[3 * k:]
            if len(remaining) == len(set(remaining)):
                return k
        return (n + 2) // 3  

        