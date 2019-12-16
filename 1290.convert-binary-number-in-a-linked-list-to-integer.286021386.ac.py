# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # Create digit_list.
        digit_list = []
        while head is not None:
            digit_list.append(head.val)
            head = head.next
        
        # Convert to decimal representation.
        digits_string = ''.join(map(str, digit_list))
        return int(digits_string, 2)

