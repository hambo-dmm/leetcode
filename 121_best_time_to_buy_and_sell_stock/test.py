import pytest

from solution import Solution

instance = Solution()

def test_case_1():
    prices = [7,1,5,3,6,4]

    assert instance.maxProfit(prices) == 5

def test_case_2():
    prices = [7,6,4,3,1]

    assert instance.maxProfit(prices) == 0    