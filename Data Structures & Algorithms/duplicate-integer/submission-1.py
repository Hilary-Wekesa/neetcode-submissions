class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return any(nums[i] in nums[i+1:] for i in range(len(nums)))