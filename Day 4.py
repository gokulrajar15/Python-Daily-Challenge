'''
There is a function signFunc(x) that returns:
1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.
Return signFunc(product).
Example 1:
Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1
'''

class Solution:
    def arraySign(self, nums):
        val = 1
        for i in nums:
            val *= i
        if val > 0:
            return 1
        elif val == 0:
            return 0
        elif val < 0:
            return -1

'''
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.
Example 1:
Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
'''


class Solution2:
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        s=set()
        for i in range(0,len(arr)-1):
            s.add(arr[i+1]-arr[i])
        if(len(s)>1):
            return False

        return True

'''
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

class Solution3:
    def isHappy(self, n: int) -> bool:
        for i in range(7):
            n = sum([int(i)**2 for i in str(n)])
        return n == 1

'''
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.
Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.
Example 1:
Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".
'''


class Solution4:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        diffs = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diffs.append(i)

        if len(diffs) != 2:
            return False

        i, j = diffs
        if s1[i] == s2[j] and s1[j] == s2[i]:
            return True

        return False
