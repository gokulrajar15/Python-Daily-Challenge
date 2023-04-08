'''
Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
Example 1:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
'''
class Solution:
    n = 11111111111111111111111111111101
    def hammingWeight(self, n: int) -> int:
        count = 0
        x = bin(n)
        for i in str(x):
            if i == "1":
                count += 1
        return count

'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
Example 1:
Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
'''

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul = 1
        sum = 0
        for i in str(n):
            mul = mul * int(i)
            sum = sum + int(i)
        return mul - sum