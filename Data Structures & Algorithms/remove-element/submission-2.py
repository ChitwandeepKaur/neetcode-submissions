class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx, last = 0, len(nums) - 1
        while idx <= last:
            if nums[idx] == val:
                nums[idx], nums[last] = nums[last], nums[idx]
                last -= 1

            else:
                idx += 1

        return idx