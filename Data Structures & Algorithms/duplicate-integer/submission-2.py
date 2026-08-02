class Solution:
        def hasDuplicate(self, nums: List[int]) -> bool:
            s = set()
            for num in nums:
                if num in s:
                    return TruTrue
                else:
                    s.add(num)
            return False
        