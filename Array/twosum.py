class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hashMap:
                return [hashMap[comp], i]
            else:
                # array value as key & index as value
                hashMap[nums[i]] = i
        return []
