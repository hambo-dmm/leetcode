import pytest
from solution import Solution

instance = Solution()

def test_case_1():
    n = 2

    assert instance.climbStairs(n) == 2

def test_case_2():
    n = 3
    
    assert instance.climbStairs(n) == 3

def test_case_3():
    n = 4

    assert instance.climbStairs(n) == 5