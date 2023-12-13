class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #convert to ints
        integerA = int(a, 2)
        integerB = int(b, 2)

        #add ints
        integerC = integerA+integerB

        #get rid of first 2 nums and convert to bstring
        c= bin(integerC)[2:]
        return c