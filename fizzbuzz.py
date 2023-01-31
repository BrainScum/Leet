class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        listerine = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                listerine.append("FizzBuzz")
            elif i % 3 == 0:
                listerine.append("Fizz")
            elif i % 5 == 0:
                listerine.append("Buzz")
            else:
                listerine.append("{}".format(i))
        return listerine

                

num = 19
example = Solution()
print(example.fizzBuzz(num))