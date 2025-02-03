class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums :
            return 0

        inclen = 1
        declen = 1
        maxlen =1 


        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inclen += 1
                declen = 1

            elif nums[i] < nums[i-1]:
                declen += 1
                inclen = 1

            else :
                inclen = declen = 1

            maxlen = max(maxlen,inclen,declen)

        return maxlen


          
        