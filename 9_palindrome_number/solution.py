class Solution:
    def isPalindrome(self, x: int) -> bool:
        #return self._string(x)
        return self._numerical(x)

    def _string(self, x):
        x = str(x)
        reversed_string = x[::-1]
        return x == reversed_string

    def _numerical(self, x):
        if x < 0:
            return False

        rev = 0
        i = x

        while i > 0:
            curr = i % 10
            rev = rev * 10 + curr
            i //= 10

        return x == rev