class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in pairs:
                return [pairs[complement], i]
            else:
                pairs[nums[i]] = i