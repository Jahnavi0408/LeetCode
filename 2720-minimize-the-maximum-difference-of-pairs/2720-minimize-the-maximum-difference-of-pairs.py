class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:




        nums.sort()  # Step 1

        def can_form_pairs(diff):  # Step 3
            count = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i+1] - nums[i] <= diff:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= p

        # Step 2
        low = 0
        high = nums[-1] - nums[0]

        # Step 4
        while low < high:
            mid = (low + high) // 2
            if can_form_pairs(mid):
                high = mid
            else:
                low = mid + 1

        return low  # Step 5
