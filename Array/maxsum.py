# O(n) run time and O(1) space complexity
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = 0
        maxSum = nums[0] # for case of all negative array 
        
        for i in range(len(nums)):
            currentSum = max(nums[i] , nums[i] + currentSum) # sets currentSum to the larger between current num and currentSum
            maxSum = max(currentSum, maxSum)
        
        return maxSum