class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        c1 = [s.index(char) for char in s]
        c2 = [t.index(char) for char in t]

        return c1 == c2 
          
        

        