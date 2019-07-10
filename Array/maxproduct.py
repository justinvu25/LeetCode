class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        localMin = localMax = globalMax = nums[0]
        
        for num in nums[1:]:
            localMinCopy = localMin
            
            localMin = min(localMin * num, num, localMax * num)
            localMax = max(localMax * num, num, localMinCopy * num)
            globalMax = max(globalMax, localMax)
        
        return globalMax