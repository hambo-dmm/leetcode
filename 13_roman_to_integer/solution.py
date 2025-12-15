class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0
        prev = 0

        # take a look at the reversed method; doesn't require the complex logic fo the previous implementation
        for i in reversed(s):
            curr = values[i]

            if curr < prev:
                result -= curr
            else:
                result += curr

            prev = curr

        return result