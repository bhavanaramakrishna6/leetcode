from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(text):
            balance = 0

            for char in text:
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1
                    if balance < 0:
                        return False

            return balance == 0

        level = {s}

        while level:
            answers = [text for text in level if is_valid(text)]

            if answers:
                return answers

            next_level = set()

            for text in level:
                for i, char in enumerate(text):
                    if char not in '()':
                        continue

                    # Removing adjacent identical parentheses
                    # produces the same string.
                    if i > 0 and char == text[i - 1]:
                        continue

                    next_level.add(text[:i] + text[i + 1:])

            level = next_level

        return []