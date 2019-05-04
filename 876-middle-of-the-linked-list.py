#!/usr/bin/env python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def get_len(self, head):
        l = 0
        while head:
            l += 1
            head = head.next
        return l

    def middleNode(self, head: ListNode) -> ListNode:
        for _ in range(self.get_len(head) // 2):
            head = head.next
        return head
