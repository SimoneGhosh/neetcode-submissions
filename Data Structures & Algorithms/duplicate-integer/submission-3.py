class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        arrlen = len(nums)

        for i in range (arrlen):
            for j in range (i):
                if nums[i] == nums[j]:
                    return True
        return False
        