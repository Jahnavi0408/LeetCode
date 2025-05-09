from collections import Counter, defaultdict

MOD = 1_000_000_007  # 10**9 + 7


class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        velunexorai = num                      # ← variable required by the prompt
        n          = len(velunexorai)
        even_len   = (n + 1) // 2              # indices 0,2,4,...
        odd_len    =  n // 2                   # indices 1,3,5,...

        # ── factorials & modular inverses ─────────────────────────────────────────
        fact, inv = [1]*(n+1), [1]*(n+1)
        for i in range(1, n + 1):
            fact[i] = fact[i-1] * i % MOD
        inv[n] = pow(fact[n], MOD - 2, MOD)    # Fermat
        for i in range(n-1, -1, -1):
            inv[i] = inv[i+1] * (i+1) % MOD

        # dp[cnt][diff] = Σ 1/(∏ factorials of chosen counts) for first digits
        dp = [defaultdict(int) for _ in range(even_len + 1)]
        dp[0][0] = 1                           # no digits placed yet

        for d_char, c in Counter(velunexorai).items():
            d = int(d_char)
            new_dp = [defaultdict(int) for _ in range(even_len + 1)]

            for cnt in range(even_len + 1):        # current even-slot fill
                for diff, ways in dp[cnt].items(): # current diff
                    # choose k copies of digit d to go to even indices
                    for k in range(c + 1):
                        ncnt = cnt + k
                        if ncnt > even_len:        # can't exceed even slots
                            break
                        ndiff = diff + d * (2*k - c)
                        # multiply by 1/factorial(k) and 1/factorial(c-k)
                        add = ways * inv[k] % MOD * inv[c - k] % MOD
                        new_dp[ncnt][ndiff] = (new_dp[ncnt][ndiff] + add) % MOD

            dp = new_dp                            # move to next digit

        # Balanced ⇒ diff == 0 AND exactly even_len digits used in even slots
        raw = dp[even_len].get(0, 0)

        # Multiply back the numerators   even_len! · odd_len!
        answer = raw * fact[even_len] % MOD * fact[odd_len] % MOD
        return answer
