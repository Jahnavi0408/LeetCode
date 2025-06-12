class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        maxdiff = 0
        for i in range(1, n):
            maxdiff = max(maxdiff, abs(nums[i] - nums[i - 1]))

        cdiff = abs(nums[0] + (nums[-1] * -1))
        maxdiff = max(maxdiff, cdiff)
        return maxdiff


        


        