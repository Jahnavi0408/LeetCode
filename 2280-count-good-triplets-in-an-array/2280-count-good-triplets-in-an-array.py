class BIT:
    def __init__(self, size):
        self.tree = [0] * (size + 2)
        self.size = size + 2
    
    def update(self, index, value):
        index += 1
        while index < self.size:
            self.tree[index] += value
            index += index & -index
    
    def query(self, index):
       
        index += 1
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        

        pos = {v: i for i, v in enumerate(nums2)}

        A = [pos[val] for val in nums1]

        left_BIT = BIT(n)
        left_smaller = [0] * n
        for i in range(n):
            left_smaller[i] = left_BIT.query(A[i] - 1)
            left_BIT.update(A[i], 1)
        

        right_BIT = BIT(n)
        right_greater = [0] * n
        for i in range(n - 1, -1, -1):
            right_greater[i] = right_BIT.query(n - 1) - right_BIT.query(A[i])
            right_BIT.update(A[i], 1)
        

        ans = 0
        for i in range(n):
            ans += left_smaller[i] * right_greater[i]
        return ans
        