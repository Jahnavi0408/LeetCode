class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        freq = list(d.values())
        return len(set(freq)) == 1

        