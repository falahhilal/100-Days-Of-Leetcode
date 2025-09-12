#https://leetcode.com/problems/reverse-linked-list/description/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        if head==None or head.next==None:
            return head
        newh=self.reverseList(head.next)
        front=head.next
        front.next=head
        head.next=None
        return newh
    

        