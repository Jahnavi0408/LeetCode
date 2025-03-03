class Solution:
    def reverseWords(self, s: str) -> str:
        words_list = s.split()

        reversed_list = words_list[::-1]  
        reversed_string = " ".join(reversed_list)

        return reversed_string

        