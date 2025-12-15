import pytest
from solution import Solution

instance = Solution()

def test_non_negative_palindrome():
    x = 121
    assert instance.isPalindrome(x) == True

def test_negative_number():
    x = -121
    assert instance.isPalindrome(x) == False

def test_non_negative_non_palindrome():
    x = 10
    assert instance.isPalindrome(x) == False
