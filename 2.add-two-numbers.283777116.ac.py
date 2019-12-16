# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        sum_list: ListNode = None
        current_list = sum_list

        while True:
            sum_val = l1.val + l2.val + carry
            if sum_val >= 10:
                carry = 1
            else:
                carry = 0
            
            new_list = ListNode(sum_val % 10)
            if current_list is None:
                sum_list = new_list
            else:
                current_list.next = new_list
            current_list = new_list
            
            if l1.next is None and l2.next is None:
                if carry == 1:
                    new_list = ListNode(1)
                    current_list.next = new_list
                    current_list = new_list
                break
            elif l1.next is None:
                l1.val = 0
                l2 = l2.next
            elif l2.next is None:
                l2.val = 0
                l1 = l1.next
            else:
                l1 = l1.next
                l2 = l2.next
        
        return sum_list
