class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr_permutation):
            if len(curr_permutation) == len(nums):
                permutations.append(curr_permutation[:])  # Dodaj kopię permutacji do wyników
                return
            for num in nums:
                if num not in curr_permutation:
                    curr_permutation.append(num)
                    backtrack(curr_permutation)
                    curr_permutation.pop()

        permutations = []
        backtrack([])
        return permutations
