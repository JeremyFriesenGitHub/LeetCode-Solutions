class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Split the input string by space and filter out empty strings
        words = s.split()
        
        # Check if there are any words in the list
        if words:
            # Return the length of the last word in the list
            return len(words[-1])
        else:
            # If no words found, return 0
            return 0
