#!/usr/bin/env python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def iter_reverse(self, head):
        pre = None
        while head:
            nxt = head.next
            head.next = pre
            pre, head = head, nxt
        return pre

    def recur_reverse(self, head):
        def aux(pre, head):
            if not head:
                return pre
            nxt = head.next
            head.next = pre
            return aux(head, nxt)
        return aux(None, head)

    def reverseList(self, head: ListNode) -> ListNode:
        return self.iter_reverse(head)
