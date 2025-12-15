import pytest
from solution import Solution

instance = Solution()

def test_case_1():
    s = "()"

    assert instance.isValid(s) == True

def test_case_2():
    s = "()[]{}"

    assert instance.isValid(s) == True

def test_case_3():
    s = "(]"

    assert instance.isValid(s) == False

def test_case_4():
    s = '([])'

    assert instance.isValid(s) == True

def test_case_5():
    s = "([)]"

    assert instance.isValid(s) == False

def test_case_6():
    s = "]"

    assert instance.isValid(s) == False

