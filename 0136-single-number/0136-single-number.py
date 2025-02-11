class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r = 0
        for i in range(len(nums)):
            r  ^= nums[i]
        return r
  
                





        