import pytest

from solution import Solution

instance = Solution()

test_cases = [
    (43261596, 964176192),
    (2147483644, 1073741822)
]

@pytest.mark.parametrize("n, expected", test_cases)
def test_cases_reversed_bits(n, expected):
    assert instance.reverseBits(n) == expected