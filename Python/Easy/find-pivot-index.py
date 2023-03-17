# https://leetcode.com/problems/find-pivot-index/

# Solution
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = rightSum = 0
        leftIndex = 0
        rightIndex = len(nums)
        if len(nums) == 1:
            return 0
        else:
            while leftIndex != rightIndex: