#简单版本
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [0]
        for i in nums:
            result.append(result[-1]+i)
        return result[1:]

#击败95%
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [0]
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums