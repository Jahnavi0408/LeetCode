class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res = set()
        for i in range(len(nums)):
            if nums[i] in res :
                return True
            res.add(nums[i])
            if i >= k:
                res.remove(nums[i-k])


        return False
            
        

        