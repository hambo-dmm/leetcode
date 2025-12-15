import pytest
from solution import Solution

instance = Solution()

def test_case_1():
    a = "11"
    b = "1"

    assert instance.addBinary(a, b) == "100"

def test_case_2():
    a = "1010"
    b = "1011"

    assert instance.addBinary(a, b) == "10101"

def test_case_3():
    a = "0"
    b = "0"

    assert instance.addBinary(a, b) == "0"