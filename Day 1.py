'''
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
Example 1:
Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
'''
class Solution:
  def countOdds(self, low: int, high: int) -> int:
    if low % 2 == 0:
        return (high-low+1)//2
    return (high-low)//2 + 1

'''
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.
Example 1:
Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500
'''
salary = [4000,3000,1000,2000]
class Solution2:
    def average(self, salary: List[int]) -> float:
        a = 0
        salary.remove(min(salary))
        salary.remove(max(salary))
        for i in salary:
            a = a + i
        return a/len(salary)