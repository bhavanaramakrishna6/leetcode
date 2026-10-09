class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        needed = 0

        for ch in s:
            if ch == '(':
                # Finish an incomplete "))" pair before opening another.
                if needed % 2 == 1:
                    insertions += 1
                    needed -= 1

                needed += 2

            else:
                needed -= 1

                # This ")" has no matching "(".
                if needed < 0:
                    insertions += 1  # Insert "(" before it.
                    needed = 1       # One more ")" completes the pair.

        return insertions + needed