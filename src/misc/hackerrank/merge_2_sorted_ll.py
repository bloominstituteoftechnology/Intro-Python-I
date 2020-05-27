"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

from leetcode
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        node_from_l1 = l1
        node_from_l2 = l2

        # To take care of edge cases where either ListNode is empty
        if not node_from_l1:
            return l2
        if not node_from_l2:
            return l1

        # Set the head of the new ll
        if node_from_l1.val <= node_from_l2.val:
            new_node = ListNode(node_from_l1.val, None)
            node_from_l1 = node_from_l1.next
        else:
            new_node = ListNode(node_from_l2.val, None)
            node_from_l2 = node_from_l2.next

        head = new_node

        # Go through the ll's to determine what should be linked next
        while node_from_l2 and node_from_l1:
            if node_from_l1.val <= node_from_l2.val:
                newest_node = ListNode(node_from_l1.val, None)
                node_from_l1 = node_from_l1.next
            else:
                newest_node = ListNode(node_from_l2.val, None)
                node_from_l2 = node_from_l2.next
            new_node.next = newest_node
            new_node = newest_node

        # Now that only 1 ll is left to go through, go ahead and add all of its nodes
        while node_from_l1:
            newest_node = ListNode(node_from_l1.val, None)
            new_node.next = newest_node
            new_node = newest_node
            node_from_l1 = node_from_l1.next

        while node_from_l2:
            newest_node = ListNode(node_from_l2.val, None)
            new_node.next = newest_node
            new_node = newest_node
            node_from_l2 = node_from_l2.next

        # print(head.val)
        return head


tail1 = ListNode(4, None)
node2 = ListNode(2, tail1)
head1 = ListNode(1, node2)

tail2 = ListNode(4, None)
node5 = ListNode(3, tail2)
head2 = ListNode(1, node5)

s = Solution()
current_node = s.mergeTwoLists(head1, head2)

while current_node:
    print(current_node.val)
    current_node = current_node.next
