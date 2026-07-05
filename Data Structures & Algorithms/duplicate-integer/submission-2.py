class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_so_far=set()
        for n in nums:
            if n not in nums_so_far:
                nums_so_far.add(n)
            else:
                return True
        return False
