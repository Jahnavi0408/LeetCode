class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        totalDistinct = len(set(nums))
        n = len(nums)
        count = 0

        for start in range(n):
            freq = defaultdict(int)
            distinctCount = 0

            for end in range(start, n):
                if freq[nums[end]] == 0:
                    distinctCount += 1
                freq[nums[end]] += 1

                if distinctCount == totalDistinct:
                    count += 1

        return count
        