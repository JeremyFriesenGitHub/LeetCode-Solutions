class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = list(s.split(" "))
        filteredString = [string for string in string if string]
        print(filteredString)
        lastWord = filteredString[len(filteredString) - 1]
        return len(lastWord)