from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted(x * x for x in nums)

        negative_count = len(nums) // 2

        return (
            sum(squares[negative_count:])
            - sum(squares[:negative_count])
        )