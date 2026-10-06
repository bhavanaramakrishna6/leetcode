class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        additions = 0

        for char in s:
            if char == '(':
                open_count += 1
            elif open_count > 0:
                open_count -= 1  # Match ')' with an earlier '('
            else:
                additions += 1  # This ')' needs a new '('

        return additions + open_count