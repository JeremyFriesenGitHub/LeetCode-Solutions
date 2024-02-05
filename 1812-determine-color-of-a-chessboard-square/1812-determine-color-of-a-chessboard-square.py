class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        #two sets
        set1=['a','c','e','g']
        set2=['b','d','f','h']

        if coordinates[0] in set1:
            if int(coordinates[1])%2 ==0:
                return True
            else:
                return False
        else:
            if int(coordinates[1])%2 ==0:
                return False
            else:
                return True

