class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        curr = 0
        min_offset = 0
        max_offset = 0

        for diff in differences:
            curr += diff
            min_offset = min(min_offset, curr)
            max_offset = max(max_offset, curr)

        
        min_start = lower - min_offset
        max_start = upper - max_offset

        
        return max(0, max_start - min_start + 1)
        