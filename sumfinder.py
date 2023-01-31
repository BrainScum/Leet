intList = [1,1,1,1,1,4,1,1,1,1,1,7,1,1,1,1,1]

class Solution:
    def twoSum(self, array, sum):
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                if array[i] + array[j] == sum:
                    return [i, j]      

solution1 = Solution()
print(solution1.twoSum(intList, 11))
