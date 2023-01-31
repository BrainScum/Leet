
def convertToRoman(num):
    numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    ans = ""
    i = len(numbers) - 1
    while i >= 0:
        temp = 0
        if num/numbers[i] >= 1:
            temp = num%numbers[i]
            ans += roman[i]*(num//numbers[i])
            num = temp
        i-=1
    return ans

print(convertToRoman(3))