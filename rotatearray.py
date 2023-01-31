class Solution:

    #basic solution

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            tempTail = nums[-1]
            nums.insert(0, tempTail)
            nums.pop()

        return nums


    #cleanest and fastest solution, but not fast enough

    def rotizlet(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0, nums.pop())
        return nums

    #splits array into two sections

    def roteezy(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        end = len(nums)
        start = len(nums) - k

        first = nums[start:end]
        last = nums[0:start]
    
        #return [*first, *last]
        return "separating attempt: " + str(first + last)


    #rotating algorithm: runs a for loop with the amount of rotations - *this was slower than my first attempt*

    def rotondra(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            #keeps a temporary variable of the last value
            temp = nums[-1]
            #start at the end of the nums array and traverse backwards
            for j in range(len(nums) - 1, 0, -1):
                #while doing this set the last value to the value before it, creating the effect of
                #rotation at the end of the array - essentially moves everything up except the first value at index 0
                nums[j] = nums[j-1]
            #sets the first value in the array to the last value (temp) to create the effect of rotation at the front
            #of the array
            nums[0] = temp
        return nums

    #works but leetcode doesn't allow reverse method

    def roti(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        start = len(nums) - k
        end = len(nums)

        first = nums[start:end]
        last = nums[0:start]

        first.reverse()
        last.reverse()

        total = last + first

        total.reverse()

        return total
    
    #great function for reversing array

    def reverse(self, nums, i, j):
        leftIndex = i
        rightIndex = j

        while leftIndex < rightIndex:
            temp = nums[leftIndex]
            nums[leftIndex] = nums[rightIndex]
            nums[rightIndex] = temp

            leftIndex += 1
            rightIndex -= 1

    def rot(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)

        if k < 0: 
            k += len(nums)

        self.reverse(nums, 0, len(nums) - k - 1)
        self.reverse(nums, len(nums) - k, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)

        return nums

listy = [1, 2, 3, 4, 5]

listy1 = list(listy)
daPhrog = [1, 2, 3, 4, 5, 6, 7]
daPhrog1 = [*daPhrog]
daPhrog2 = [*daPhrog]
daPhrog3 = list(daPhrog.copy())
daPhrog4 = [*daPhrog]
daFinalPhrog = (list(daPhrog4)).copy()

rup = list(map(lambda n: n, [1, 2, 3, 4, 5, 6, 7]))

#print(Solution.rotate(object, daPhrog, 3))

#print(Solution.roteezy(object, daPhrog1, 3))

#print(Solution.rotondra(object, daPhrog2, 3))

#print(Solution.rotizlet(object, daPhrog3, 3))

print(Solution.roti(object, rup, 3))

example = Solution()

print(example.rot(rup, 3))