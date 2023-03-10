# https://leetcode.com/problems/running-sum-of-1d-array/

# Solution
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = [nums[0]]
        for i in range(1, len(nums)):
            runningSum.append(runningSum[i-1]+nums[i])
        return runningSum