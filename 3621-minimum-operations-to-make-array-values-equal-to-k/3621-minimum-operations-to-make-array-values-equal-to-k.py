class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        numsSet = set(nums)
        mn = min(numsSet)
        if mn < k:
            return -1
        elif mn > k:
            return len(numsSet)
        else:
            return len(numsSet) - 1



                
