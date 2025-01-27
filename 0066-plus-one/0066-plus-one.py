class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res =[]
        n = int("".join(map(str,digits)))
        n = n+ 1
        for d in str(n):
            res.append(int(d))
        return res


        