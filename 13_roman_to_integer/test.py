import pytest
from solution import Solution

instance = Solution()

def test_case_III():
    s = "III"
    
    assert instance.romanToInt(s) == 3

def test_case_LVIII():
    s = "LVIII"

    assert instance.romanToInt(s) == 58

def test_case_MCMXCIV():
    s = "MCMXCIV"

    assert instance.romanToInt(s) == 1994

def test_case_IX():
    s = "IX"

    assert instance.romanToInt(s) == 9