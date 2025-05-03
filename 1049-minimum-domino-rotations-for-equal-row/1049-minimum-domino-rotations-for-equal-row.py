class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        if len(tops) != len(bottoms): return -1
        same, countA, countB = Counter(), Counter(tops), Counter(bottoms)
        for a, b in zip(tops, bottoms):
            if a == b:
                same[a] += 1
        for i in range(1, 7):
            if countA[i] + countB[i] - same[i] == len(tops):
                return min(countA[i], countB[i]) - same[i]        
        return -1
        