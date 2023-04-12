
'''
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
'''
import null as null

root = [1,null,3,2,4,null,5,6]
class Solution:
    def preorder(self, root):
        if not root:
            return []

        stack, result = [root], []

        while stack:
            node = stack.pop()
            result.append(node.val)
            for child in reversed(node.children):
                stack.append(child)

        return result
'''
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
'''
class Solution1:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}
        for num in reversed(nums2):
            while stack and num > stack[-1]:
                stack.pop()
            next_greater[num] = stack[-1] if stack else -1
            stack.append(num)

        return [next_greater[num] for num in nums1]

'''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
'''
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x1, y1), (x2, y2) = coordinates[:2]
        for i in range(2, len(coordinates)):
            (x, y) = coordinates[i]
            if((y2 - y1) * (x1 - x) != (y1 - y) * (x2 - x1)):
                return False
        return True