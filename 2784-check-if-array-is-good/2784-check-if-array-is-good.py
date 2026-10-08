from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        expected = list(range(1, n + 1)) + [n]

        return sorted(nums) == expected