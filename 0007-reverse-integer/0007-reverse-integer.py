class Solution:
    def reverse(self, x: int) -> int:
        result = 0

        while x != 0:
            # Extract the last digit, preserving its sign
            digit = x % 10 if x > 0 else x % -10

            # Remove the last digit
            x = (x - digit) // 10

            # Check the upper 32-bit limit
            if result > 214748364 or (
                result == 214748364 and digit > 7
            ):
                return 0

            # Check the lower 32-bit limit
            if result < -214748364 or (
                result == -214748364 and digit < -8
            ):
                return 0

            result = result * 10 + digit

        return result