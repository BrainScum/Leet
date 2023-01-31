class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        sum = 0
        highestWealth = 0

        for i in range(0, len(accounts)):
            for j in range(0, len(accounts[i])):
                sum += accounts[i][j]
            
            if sum > highestWealth:
                highestWealth = sum

            sum = 0
        return highestWealth


#2d traverse over the array
#variable that keeps track of the highest recorded wealth - if a new account (sum of j) has more, update the variable

accounts1 = [[1, 3, 4], [2, 6, 7]]

example = Solution()
print(example.maximumWealth(accounts1))