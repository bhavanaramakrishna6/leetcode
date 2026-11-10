from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        one_back = 0
        two_back = three_back = float("inf")

        for i in range(n):
            current = costs[i] + min(
                one_back + 1,
                two_back + 4,
                three_back + 9,
            )
            one_back, two_back, three_back = current, one_back, two_back

        return one_back