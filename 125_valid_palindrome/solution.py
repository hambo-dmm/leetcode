class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed_s = "".join(
            char.lower() for char in s if char.isalnum()
        )

        return processed_s == processed_s[::-1]