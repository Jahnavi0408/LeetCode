class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        match = strs[0]
        preflen = len(match)

        for s in strs[1:]:
            while match != s[0:preflen]:
                preflen -= 1
                if preflen == 0:
                    return ""

                match = match[0:preflen]

        return match

            
            

        

