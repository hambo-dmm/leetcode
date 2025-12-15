import pytest

from solution import Solution
from TreeNode import TreeNode

instance = Solution()

def test_case_1():
    root = [1,2,3,4,5]
    binaryTree = TreeNode.make_binary_tree(root)

    assert instance.diameterOfBinaryTree(binaryTree) == 3


def test_case_2():
    root = [1,2]
    binaryTree = TreeNode.make_binary_tree(root)

    assert instance.diameterOfBinaryTree(binaryTree) == 1

def test_case_3():
    root = [1,2,3,4,5,6,7,8,9,10,11]
    binaryTree = TreeNode.make_binary_tree(root)

    assert instance.diameterOfBinaryTree(binaryTree) == 5
