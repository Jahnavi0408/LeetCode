class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        from itertools import product
        MOD = 10**9 + 7

        # Generate all valid column states: adjacent colors in a column must differ
        def is_valid(col):
            return all(col[i] != col[i+1] for i in range(m - 1))

        valid_states = [state for state in product(range(3), repeat=m) if is_valid(state)]
        state_index = {state: i for i, state in enumerate(valid_states)}
        num_states = len(valid_states)

        # Precompute compatibility: two columns are compatible if their colors differ at all rows
        compatible = [[] for _ in range(num_states)]
        for i, a in enumerate(valid_states):
            for j, b in enumerate(valid_states):
                if all(x != y for x, y in zip(a, b)):
                    compatible[i].append(j)

        # DP initialization
        dp = [1] * num_states

        for _ in range(n - 1):
            new_dp = [0] * num_states
            for i in range(num_states):
                for j in compatible[i]:
                    new_dp[j] = (new_dp[j] + dp[i]) % MOD
            dp = new_dp

        return sum(dp) % MOD
