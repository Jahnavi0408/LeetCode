class Solution:
    def maxDifference(self, s: str) -> int:
        # Solution 2: Slight performance optimizations
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1
        max_odd = 0
        min_even = float('inf')
        for f in freq:
            if f & 1:
                if f > max_odd:
                    max_odd = f
            elif f:
                if f < min_even:
                    min_even = f
        return max_odd - min_even


        # Solution 1: Easy first approach
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1
        odds = [f for f in freq if f % 2 == 1]
        evens = [f for f in freq if f % 2 == 0 and f > 0]
        return max(odds) - min(evens)