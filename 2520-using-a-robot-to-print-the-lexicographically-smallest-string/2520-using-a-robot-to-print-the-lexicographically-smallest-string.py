class Solution:
    def robotWithString(self, s: str) -> str:
        
        count = Counter(s)  # Frequency of remaining characters in s
        stack = []
        result = []
        min_char = 'a'
        
        for ch in s:
            stack.append(ch)
            count[ch] -= 1
            
            # Update min_char to the smallest available in remaining s
            while min_char <= 'z' and count[min_char] == 0:
                min_char = chr(ord(min_char) + 1)
            
            # Pop from stack to result as long as top is <= min_char
            while stack and stack[-1] <= min_char:
                result.append(stack.pop())
        
        # Add any remaining characters in stack
        while stack:
            result.append(stack.pop())
        
        return ''.join(result)
