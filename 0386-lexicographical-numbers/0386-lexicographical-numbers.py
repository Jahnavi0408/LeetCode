class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        res = []
        num = 1
        for _ in range(n):
            res.append(num)
            if num * 10 <= n:
                num *= 10  # Go deeper
            else:
                while num % 10 == 9 or num >= n:
                    num //= 10  # Go back up
                num += 1  # Move to the next number
        return res
        