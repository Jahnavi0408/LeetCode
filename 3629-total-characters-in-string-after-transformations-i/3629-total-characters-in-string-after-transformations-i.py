class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        count = [0] * 26
        
        for c in s:
            count[ord(c) - ord('a')] += 1

        for _ in range(t):
            new_count = [0] * 26
            for i in range(25): 
                new_count[i + 1] = count[i]
            z_count = count[25] 
            new_count[0] = (new_count[0] + z_count) % MOD  
            new_count[1] = (new_count[1] + z_count) % MOD 
            count = new_count

        return sum(count) % MOD