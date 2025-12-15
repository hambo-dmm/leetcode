import pytest

from solution import Solution

instance = Solution()

test_cases = [
    (11, 3),
    (128, 1),
    (2147483645, 30)
]

@pytest.mark.parametrize("n, expected", test_cases)
def test_cases_hamming_weight(n, expected):
    assert instance.hammingWeight(n) == expected