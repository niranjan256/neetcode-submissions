class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []

        def backtrack(i):
            if i == len(nums):
                res.append(sol[:])
                return

            # Pick nums[i] (LEFT)
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

            # Don't pick nums[i] (RIGHT)
            backtrack(i + 1)

        backtrack(0)
        return res