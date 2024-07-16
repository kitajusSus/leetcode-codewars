class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start=0):
            if start == len(nums):
                res.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        
        res = []
        if len(nums) == 1:
            return [nums.copy()]
        backtrack()
        return res
#link :https://leetcode.com/submissions/detail/1322863652/
