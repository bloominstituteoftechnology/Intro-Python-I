# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):

# fff
import collections


def inorderTraversal(self, root):
    max = 0
    res = []
    if root:
        res = self.inorderTraversal(root.left)
        if root.val > max:
            res.append(root.val)
        res = res + self.inorderTraversal(root.right)
    return res


list = [1, 2, 3]
for l in list:
    print(l, end=' ')


def is_balanced_binary_tree(tree):
    BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight', ('balanced', 'height'))

    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(True, - 1)  # Base Case

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return BalancedStatusWithHeight(False, 0)
        # if difference of height is 0 or 1
        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balanced(tree).balanced
