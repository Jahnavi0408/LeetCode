class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                count += 1
            if count >= 2:
                return False
        if nums[len(nums)-1] > nums[0] and count >=1:
            return False
        return True