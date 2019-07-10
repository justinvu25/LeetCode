# O(n) time & space complexity
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        # creating 3 empty arrays the length of the nums array
        left, right, answer = [0]*length, [0]*length, [0]*length

        left[0] = 1 # first index of left array is 1 because there's nothing left of first index of nums

        for i in range(1, length):
            left[i] = nums[i - 1] * left[i - 1] # multiply previous nums value with previous result of left array

        right[length - 1] = 1

        for i in reversed(range(length - 1)):
            right[i] = nums[i + 1] * right[i + 1]

        for i in range(length):
            answer[i] = left[i] * right[i]

        return answer

# O(1) space complexity
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)

        answer = [0] * length

        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i-1]

        right = 1 # keep track of running product

        for i in reversed(range(length)):
            answer[i] = answer[i] * right
            right *= nums[i]

        return answer
