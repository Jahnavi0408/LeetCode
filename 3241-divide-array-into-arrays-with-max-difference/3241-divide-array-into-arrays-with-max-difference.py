from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()                       # 1. sort in non-decreasing order
        res: List[List[int]] = []
        
        for i in range(0, len(nums), 3):  
            if nums[i + 2] - nums[i] > k:  # max – min within the triple
                return []                 #    → impossible overall
            res.append([nums[i], nums[i + 1], nums[i + 2]])
        
        return res

        