class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total_sum = n * (n + 1) // 2
        k = n // m
        divisible_sum = m * k * (k + 1) // 2
        non_divisible_sum = total_sum - divisible_sum
        return non_divisible_sum - divisible_sum

        