class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numhash = {}
        for (i, num) in enumerate(nums):
            complement = target - num
            if complement in numhash:
                return [numhash[complement], i]
            numhash[num] = i