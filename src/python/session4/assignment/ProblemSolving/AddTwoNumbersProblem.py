#https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype result: Optional[ListNode]
        """
        carry = 0
        dummy = ListNode(0)
        current = dummy
        while  l1 is not None or l2 is not None or carry != 0:
            value1 = l1.val if l1 else 0

            value2 = l2.val if l2 else 0

            sum = value1 + value2 + carry
            carry = sum//10  
            digit = sum%10   
 
            new_Node = ListNode(digit) 
 
            current.next = new_Node 
            current = new_Node 
 
            if l1: 
              l1 = l1.next 
     
            if l2: 
              l2 =  l2.next
 
        return dummy.next
