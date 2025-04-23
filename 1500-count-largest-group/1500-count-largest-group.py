class Solution:
    def countLargestGroup(self, n: int) -> int:
        def digit_sum(x):
            return sum(int(d) for d in str(x))

        group_sizes = defaultdict(int)

        for num in range(1, n + 1):
            s = digit_sum(num)
            group_sizes[s] += 1

        max_size = max(group_sizes.values())
        return sum(1 for size in group_sizes.values() if size == max_size)
            