# https://leetcode.com/problems/binary-search/

# Solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        lowIndex = 0
        highIndex = len(nums)-1

        if nums[lowIndex] ==target:
            return lowIndex
        if nums[highIndex] == target:
            return highIndex

        pivot = (lowIndex + highIndex)//2

        while pivot != lowIndex and pivot != highIndex:
            
            if nums[pivot] == target:
                return pivot

            if nums[pivot] > target:
                highIndex = pivot
            elif nums[pivot] < target:
                lowIndex = pivot
            pivot = (lowIndex + highIndex)//2

        return -1
