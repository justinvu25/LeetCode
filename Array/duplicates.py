# set solution, O(n) time & space complexity
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for num in nums:
            if num in hashSet:
                return True
            else:
                hashSet.add(num)
        return False


# sorting solution O(nlogn) solution (assuming sort is heap sort), O(1) space complexity
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
