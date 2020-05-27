"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

from leetcode
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        val1 = ''
        current_node = l1
        while current_node:
            val1 = str(current_node.val) + val1
            current_node = current_node.next
        # print(val1)

        val2 = ''
        current_node = l2
        while current_node:
            val2 = str(current_node.val) + val2
            current_node = current_node.next
        # print(val2)

        result = int(val1) + int(val2)
        # print(result)
        tail = ListNode(str(result)[0], None)

        # print(tail.val)
        current_node = tail
        for digit in str(result)[1:]:
            # print(digit)
            new_node = ListNode(digit, current_node)
            current_node = new_node

        # print(current_node.val)
        return(current_node)


s = Solution()
node3 = ListNode(3, None)
node2 = ListNode(4, node3)
node1 = ListNode(2, node2)

node6 = ListNode(4, None)
node5 = ListNode(6, node6)
node4 = ListNode(5, node5)

s.addTwoNumbers(node1, node4)
