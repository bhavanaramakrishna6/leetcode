from typing import List

class Solution:
    def minSumSquareDiff(
        self, nums1: List[int], nums2: List[int],
        k1: int, k2: int
    ) -> int:
        k = k1 + k2
        max_diff = max(abs(a - b) for a, b in zip(nums1, nums2))
        count = [0] * (max_diff + 1)
        total_diff = 0

        for a, b in zip(nums1, nums2):
            d = abs(a - b)
            count[d] += 1
            total_diff += d

        # Enough operations to make every pair equal.
        if k >= total_diff:
            return 0

        for d in range(max_diff, 0, -1):
            if k == 0:
                break

            # Reduce this many differences from d to d - 1.
            moves = min(count[d], k)
            count[d] -= moves
            count[d - 1] += moves
            k -= moves

        return sum(d * d * freq for d, freq in enumerate(count))