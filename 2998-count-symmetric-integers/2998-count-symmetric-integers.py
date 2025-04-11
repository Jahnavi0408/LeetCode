class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high + 1):
            s = str(num)
            if len(s) % 2 == 0:
                n = len(s) // 2
                first_half_sum = sum(int(d) for d in s[:n])
                second_half_sum = sum(int(d) for d in s[n:])
                if first_half_sum == second_half_sum:
                    count += 1
        return count