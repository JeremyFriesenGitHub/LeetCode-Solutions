class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = -1
        for i in range(len(accounts)):
            summer = sum(accounts[i])
            if summer > max:
                max = summer
        return max