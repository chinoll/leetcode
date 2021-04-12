class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [0]
        for i in nums:
            result.append(result[-1]+i)
        return result[1:]