class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        total_pairs = 0
        left = 0
        res = 0

        for right in range(len(nums)):
            num = nums[right]
            total_pairs += count[num] 
            count[num] += 1

            while total_pairs >= k:
                res += len(nums) - right  
                count[nums[left]] -= 1
                total_pairs -= count[nums[left]] 
                left += 1

        return res
            