#https://leetcode.com/problems/odd-even-linked-list/description/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if head==None or head.next==None or head.next.next==None:
            return head
        
        odd=head
        even=head.next
        curr=head.next.next
        even_head=even
        i=3

        while curr:
            if i%2==0:
                even.next=curr
                even=even.next
            else:
                odd.next=curr
                odd=odd.next

            curr=curr.next
            i+=1

        if i%2==0:
            even.next=curr

        odd.next=even_head

        return head