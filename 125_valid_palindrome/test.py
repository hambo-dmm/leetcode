import pytest

from solution import Solution

instance = Solution()

def test_case_1():
    s = "A man, a plan, a canal: Panama"

    assert instance.isPalindrome(s) == True


def test_case_2():
    s = "race a car"

    assert instance.isPalindrome(s) == False


def test_case_3():
    s = " "

    assert instance.isPalindrome(s) == True