#https://leetcode.com/problems/add-two-numbers/description/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1 = 0
        m = 1
        while l1:
            num1 += l1.val * m
            m *= 10
            l1 = l1.next
        
        num2 = 0
        x = 1
        while l2:
            num2 += l2.val * x
            x *= 10
            l2 = l2.next
        
        total = num1 + num2
        
        temp =ListNode()
        current =temp
        
        if total ==0:
            return ListNode(0)
        
        while total >0:
            digit =total % 10
            current.next =ListNode(digit)
            current =current.next
            total //=10

        return temp.next    