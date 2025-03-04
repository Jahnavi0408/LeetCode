class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # c1 = [s.index(char) for char in s]
        # c2 = [t.index(char) for char in t]

        # return c1 == c2 

        mapst = {}
        mapts = {}

        for chs, cht in zip(s,t):
            if chs in mapst and mapst[chs] != cht:
                return False
            if cht in mapts and mapts[cht] != chs:
                return False

            mapst[chs] = cht
            mapts[cht] = chs

        return True
            
        
          
        

        