def runningSum(arr):
    newArr = []
    sum = 0
    for i in range(0, len(arr)):
        sum += arr[i]
        newArr.append(sum)
        
    return newArr

listerine = [1, 3, 6, 8]
print(runningSum(listerine))

