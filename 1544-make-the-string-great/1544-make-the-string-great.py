class Solution:
    def makeGood(self, s: str) -> str:
        made_change = True  # Initialize with True to enter the loop
        while made_change:  # Continue until no changes are made
            made_change = False  # Assume no change will be made
            i = 0  # Start from the beginning of the string
            while i < len(s) - 1:
                # Check if the current and next characters are a lowercase-uppercase pair
                if (s[i].islower() and s[i].upper() == s[i+1]) or (s[i].isupper() and s[i].lower() == s[i+1]):
                    s = s[:i] + s[i+2:]  # Remove the pair
                    made_change = True  # Mark that a change was made
                    # Do not increment i here, since we want to check the new pair formed at the current index
                else:
                    i += 1  # Move to the next character only if no pair was removed
        return s
        
        