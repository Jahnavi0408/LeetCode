from typing import List
from collections import Counter
import math

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        total_rabbits = 0

        for answer, freq in count.items():
            group_size = answer + 1
            groups = math.ceil(freq / group_size)
            total_rabbits += groups * group_size

        return total_rabbits
        