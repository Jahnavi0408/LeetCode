from collections import Counter
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        length = 0
        central = False

        for word in count:
            rev = word[::-1]
            if word != rev:
                if rev in count:
                    pair_count = min(count[word], count[rev])
                    length += pair_count * 4
                    count[word] -= pair_count
                    count[rev] -= pair_count
            else:
                pair_count = count[word] // 2
                length += pair_count * 4
                count[word] -= pair_count * 2
                if count[word] > 0:
                    central = True

        if central:
            length += 2

        return length
