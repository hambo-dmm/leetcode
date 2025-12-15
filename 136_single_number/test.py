import pytest

from solution import Solution

instance = Solution()

def test_case_1():
    nums = [2,2,1]

    assert instance.singleNumber(nums) == 1

def test_case_2():
    nums = [4,1,2,1,2]

    assert instance.singleNumber(nums) == 4

def test_case_3():
    nums = [1]

    assert instance.singleNumber(nums) == 1