class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = Counter(digits)
        result = []

        for num in range(100, 1000):
            if num % 2 != 0:
                continue  
            c = Counter(map(int, str(num)))
            if all(count[d] >= c[d] for d in c):
                result.append(num)
        
        return result
        
