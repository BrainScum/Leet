class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        #keep a counter of steps
        #if it is even: divide by 2, if it is odd: subtract 1
        #variable that keeps track of num
        counter = 0

        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            
            counter+=1
        return counter
            
    
num = 6
example = Solution()
print(example.numberOfSteps(num))