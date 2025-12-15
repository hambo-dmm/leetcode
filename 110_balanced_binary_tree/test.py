import pytest

from solution import Solution
from TreeNode import TreeNode

instance = Solution()

def test_case_1():
    root = [3,9,20,None,None,15,7]
    binary_tree = TreeNode.make_binary_tree(root)

    assert instance.isBalanced(binary_tree) == True

def test_case_2():
    root = [1,2,2,3,3,None,None,4,4]
    binary_tree = TreeNode.make_binary_tree(root)

    assert instance.isBalanced(binary_tree) == False

def test_case_3():
    root = []
    binary_tree = TreeNode.make_binary_tree(root)

    assert instance.isBalanced(binary_tree) == True