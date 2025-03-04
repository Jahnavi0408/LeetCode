class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        match = strs[0]
        prevlen = len(match)

        for s in strs[1:]:
            while match != s[0:prevlen]:
                prevlen -= 1
                if prevlen == 0:
                    return ""

                match = match[0:prevlen]

        return match
















            
            

        

