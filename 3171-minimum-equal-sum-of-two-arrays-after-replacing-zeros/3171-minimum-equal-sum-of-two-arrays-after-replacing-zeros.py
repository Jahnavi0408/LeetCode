from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(x for x in nums1 if x != 0)
        sum2 = sum(x for x in nums2 if x != 0)
        zero1 = nums1.count(0)
        zero2 = nums2.count(0)

        min1 = sum1 + zero1
        min2 = sum2 + zero2

        target = max(min1, min2)


        if (target - sum1 > 0 and zero1 == 0) or (target - sum2 > 0 and zero2 == 0):
            return -1
        if (target - sum1) < zero1 or (target - sum2) < zero2:
            return -1

        return target

