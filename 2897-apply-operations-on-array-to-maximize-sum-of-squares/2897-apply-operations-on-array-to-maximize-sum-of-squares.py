from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_count = [0] * 30

        # Count how many numbers have each bit set.
        for num in nums:
            for bit in range(30):
                if num & (1 << bit):
                    bit_count[bit] += 1

        answer = 0

        # Build k numbers using the available bits.
        for _ in range(k):
            value = 0

            for bit in range(30):
                if bit_count[bit] > 0:
                    value |= (1 << bit)
                    bit_count[bit] -= 1

            answer = (answer + value * value) % MOD

        return answer